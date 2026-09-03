from flask import Flask, render_template, request, redirect, url_for, abort
from modules.student_manager import (
    get_all_students,
    get_student_by_id,
    add_student,
    update_student,
    delete_student
)

from modules.dataset_manager import (
    get_all_datasets,
    get_dataset_by_name,
    create_dataset,
    add_student_record,
    delete_dataset
)
from modules.config_loader import load_config
from modules.analytics import (
rank_students,get_topper,get_lowest_performer,get_weak_students,get_dataset_statistics,
get_subject_averages,get_strongest_subject_overall,get_weakest_subject_overall,evaluate_student_record,evaluate_dataset_records
)
from modules.intelligence.history import get_student_academic_history
from modules.intelligence.performance import build_student_performance_series
from modules.intelligence.trends import analyze_student_trend
from modules.intelligence.risk import analyze_student_risk
from modules.intelligence.prediction import predict_student_performance
from modules.intelligence.advanced_analysis import (
    compare_internal_board_performance,
    analyze_weakness_persistence,
    analyze_academic_stability,
    analyze_improvement_momentum,
    analyze_subject_comovement,
    analyze_exam_context,
    analyze_cohort_performance,
    analyze_subject_consistency
)
from modules.insights import generate_student_insights 
from modules.intelligence.history import get_student_record_from_dataset


app = Flask(__name__)


@app.route("/")
def home():
    students = get_all_students()
    datasets = get_all_datasets()

    student_count = len(students)
    dataset_count = len(datasets)

    total_records = 0

    for dataset in datasets:
        total_records += len(dataset.get("records", []))

    return render_template(
        "index.html",
        students=students,
        datasets=datasets,
        student_count=student_count,
        dataset_count=dataset_count,
        total_records=total_records
    )



@app.route("/students")
def students():
    students = get_all_students()

    return render_template(
        "students.html",
        students=students
    ) 


@app.route("/students/<int:student_id>")
def student_detail(student_id):
    student = get_student_by_id(student_id)

    if not student:
        abort(404)

    return render_template(
        "student_detail.html",
        student=student
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404 

@app.route("/students/add", methods=["GET", "POST"])
def add_student_page():

    if request.method == "POST":

        student_id = int(request.form["student_id"])
        name = request.form["name"]
        institution = request.form["institution"]
        section = request.form["section"]
        board = request.form["board"]
        batch = int(request.form["batch"])
        class_roll = int(request.form["class_roll"])

        board_roll = request.form.get("board_roll")
        board_registration = request.form.get("board_registration")

        result = add_student(
            student_id,
            name,
            institution,
            section,
            board,
            batch,
            class_roll,
            board_roll,
            board_registration
        )

        if result["status"] == "success":
            return redirect(url_for("students"))

        return render_template(
            "add_student.html",
            error=result["message"]
        )

    return render_template("add_student.html")


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student_page(student_id):

    student = get_student_by_id(student_id)

    if not student:
        return render_template("404.html"), 404

    if request.method == "POST":

        name = request.form["name"]
        institution = request.form["institution"]
        section = request.form["section"]
        board = request.form["board"]
        batch = int(request.form["batch"])
        class_roll = int(request.form["class_roll"])

        board_roll = request.form.get("board_roll")
        board_registration = request.form.get("board_registration")

        result = update_student(
            student_id,
            name,
            institution,
            section,
            board,
            batch,
            class_roll,
            board_roll,
            board_registration
        )

        if result["status"] == "success":
            return redirect(
                url_for("student_detail", student_id=student_id)
            )

        return render_template(
            "edit_student.html",
            student=student,
            error=result["message"]
        )

    return render_template(
        "edit_student.html",
        student=student
    )


@app.route("/students/<int:student_id>/delete", methods=["POST"])
def delete_student_page(student_id):

    result = delete_student(student_id)

    if result["status"] == "success":
        return redirect(url_for("students"))

    student = get_student_by_id(student_id)

    return render_template(
        "student_detail.html",
        student=student,
        error=result["message"]
    ) 







@app.route("/datasets")
def datasets():
    datasets = get_all_datasets()
    return render_template("datasets.html", datasets=datasets)

@app.route("/datasets/<exam_name>")
def dataset_detail(exam_name):
    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    return render_template("dataset_detail.html", dataset=dataset)



@app.route("/datasets/create", methods=["GET", "POST"])
def create_dataset_page():

    if request.method == "POST":
        exam_name = request.form["exam_name"]
        exam_date = request.form["exam_date"]
        dataset_type = request.form["dataset_type"]
        batch = int(request.form["batch"])

        if dataset_type == "internal":
            institution = request.form["institution"]
            board = None

        else:
            institution = None
            board = request.form["board"]

        result = create_dataset( exam_name,exam_date,dataset_type,institution, board,batch)

        if result["status"] == "success":
            return redirect(url_for("datasets"))

        return render_template(
            "create_dataset.html",
            error=result["message"]
        )

    return render_template("create_dataset.html")




@app.route("/datasets/<exam_name>/add-record", methods=["GET", "POST"])
def add_record_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    if request.method == "POST":
        student_id = int(request.form["student_id"])

        marks = {}

        for subject in config["subjects"]:
            marks[subject] = int(request.form[subject])

        result = add_student_record(
            exam_name,
            student_id,
            marks
        )

        if result["status"] == "success":
            return redirect(
                url_for("dataset_detail", exam_name=exam_name)
            )

        return render_template(
            "add_record.html",
            dataset=dataset,
            subjects=config["subjects"],
            error=result["message"]
        )

    return render_template(
        "add_record.html",
        dataset=dataset,
        subjects=config["subjects"]
    )
@app.route("/datasets/<exam_name>/delete", methods=["POST"])
def delete_dataset_page(exam_name):

    result = delete_dataset(exam_name)

    if result["status"] == "success":
        return redirect(url_for("datasets"))

    dataset = get_dataset_by_name(exam_name)

    return render_template(
        "dataset_detail.html",
        dataset=dataset,
        error=result["message"]
    ) 

@app.route("/analytics", methods=["GET", "POST"])
def analytics():
    datasets = get_all_datasets()

    if request.method == "POST":
        exam_name = request.form["exam_name"]

        return redirect(
            url_for("analytics_dataset", exam_name=exam_name)
        )

    return render_template(
        "analytics.html",
        datasets=datasets
    )


@app.route("/analytics/<exam_name>")
def analytics_dataset(exam_name):
    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    subject_averages = get_subject_averages(dataset)

    ranked_students = rank_students(dataset, config)
    top_students = ranked_students[:5]

    evaluated_students = evaluate_dataset_records(dataset, config)
    statistics = get_dataset_statistics(dataset, config)

    return render_template(
    "analytics_dataset.html",
    dataset=dataset,
    subject_averages=subject_averages,
    top_students=top_students,
    evaluated_students=evaluated_students,
    statistics=statistics
      )

@app.route("/analytics/<exam_name>/rank", methods=["POST"])
def rank_students_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    ranked_students = rank_students(dataset, config)

    return render_template(
        "ranked_students.html",
        dataset=dataset,
        ranked_students=ranked_students
    )

@app.route("/analytics/<exam_name>/top-performer", methods=["POST"])
def top_performer_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    topper = get_topper(dataset, config)

    return render_template(
        "top_performer.html",
        dataset=dataset,
        topper=topper
    ) 

@app.route("/analytics/<exam_name>/lowest-performer", methods=["POST"])
def lowest_performer_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    student = get_lowest_performer(dataset, config)

    return render_template(
        "lowest_performer.html",
        dataset=dataset,
        student=student
    )

@app.route("/analytics/<exam_name>/weak-students", methods=["POST"])
def weak_students_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    weak_students = get_weak_students(dataset, config)

    return render_template(
        "weak_students.html",
        dataset=dataset,
        weak_students=weak_students
    ) 


@app.route("/analytics/<exam_name>/statistics", methods=["POST"])
def dataset_statistics_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    config = load_config()

    statistics = get_dataset_statistics(dataset, config)

    return render_template(
        "dataset_statistics.html",
        dataset=dataset,
        statistics=statistics
    ) 

@app.route("/analytics/<exam_name>/subject-averages", methods=["POST"])
def subject_averages_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    subject_averages = get_subject_averages(dataset)

    return render_template(
        "subject_averages.html",
        dataset=dataset,
        subject_averages=subject_averages
    ) 

@app.route("/analytics/<exam_name>/strongest-subject", methods=["POST"])
def strongest_subject_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    strongest_subject = get_strongest_subject_overall(dataset)

    return render_template(
        "strongest_subject.html",
        dataset=dataset,
        strongest_subject=strongest_subject
    )  

@app.route("/analytics/<exam_name>/weakest-subject", methods=["POST"])
def weakest_subject_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    weakest_subject = get_weakest_subject_overall(dataset)

    return render_template(
        "weakest_subject.html",
        dataset=dataset,
        weakest_subject=weakest_subject
    ) 

@app.route("/analytics/<exam_name>/evaluate")
def evaluate_student_page(exam_name):

    dataset = get_dataset_by_name(exam_name)

    if not dataset:
        return render_template("404.html"), 404

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "evaluate_student.html",
            dataset=dataset
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "evaluate_student.html",
            dataset=dataset,
            error="Student ID must be an integer."
        )

    student_record = get_student_record_from_dataset(
        dataset,
        student_id
    )

    if not student_record:
        return render_template(
            "evaluate_student.html",
            dataset=dataset,
            error="Student not found in this dataset."
        )

    config = load_config()

    evaluation = evaluate_student_record(
        student_record,
        config
    )

    return render_template(
        "evaluate_student.html",
        dataset=dataset,
        evaluation=evaluation
    )

@app.route("/academic-intelligence")
def academic_intelligence():

    return render_template("academic_intelligence.html") 


@app.route("/academic-intelligence/history")
def academic_history():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = get_student_academic_history(student_id)

    return render_template(
        "academic_history.html",
        result=result
    )

@app.route("/academic-intelligence/performance")
def academic_performance():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = build_student_performance_series(student_id)

    return render_template(
        "academic_performance.html",
        result=result
    )


@app.route("/academic-intelligence/trend")
def academic_trend():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = analyze_student_trend(student_id)

    return render_template(
        "academic_trend.html",
        result=result
    )

@app.route("/academic-intelligence/risk")

def academic_risk():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = analyze_student_risk(student_id)

    return render_template(
        "academic_risk.html",
        result=result
    )
@app.route("/academic-intelligence/prediction")
def academic_prediction():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = predict_student_performance(student_id)

    return render_template(
        "academic_prediction.html",
        result=result
    ) 

@app.route("/academic-intelligence/insights")
def academic_insights():

    student_id = request.args.get("student_id")

    if not student_id:
        return redirect(url_for("academic_intelligence"))

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_intelligence.html",
            error="Student ID must be an integer."
        )

    result = generate_student_insights(student_id)

    return render_template(
        "academic_insights.html",
        result=result
    ) 



@app.route("/academic-intelligence/internal-board")
def internal_board_comparison():

    

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "internal_board.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "internal_board.html",
            error="Student ID must be an integer."
        )

    datasets = get_all_datasets()

    internal_datasets = []
    board_datasets = []

    for dataset in datasets:

        if dataset["type"] == "internal":
            internal_datasets.append(dataset)

        elif dataset["type"] == "board":
            board_datasets.append(dataset)

    internal_exam = request.args.get("internal_exam")
    board_exam = request.args.get("board_exam")

    result = None

    if internal_exam and board_exam:
        result = compare_internal_board_performance(
            student_id,
            internal_exam,
            board_exam
        )

    return render_template(
        "internal_board.html",
        student_id=student_id,
        internal_datasets=internal_datasets,
        board_datasets=board_datasets,
        result=result
    ) 

@app.route("/academic-intelligence/weakness-persistence")
def weakness_persistence():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "weakness_persistence.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "weakness_persistence.html",
            error="Student ID must be an integer."
        )

    result = analyze_weakness_persistence(student_id)

    return render_template(
        "weakness_persistence.html",
        result=result,
        student_id=student_id
    ) 

@app.route("/academic-intelligence/stability")
def academic_stability():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "academic_stability.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "academic_stability.html",
            error="Student ID must be an integer."
        )

    result = analyze_academic_stability(student_id)

    return render_template(
        "academic_stability.html",
        result=result,
        student_id=student_id
    ) 


@app.route("/academic-intelligence/momentum")
def improvement_momentum():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "improvement_momentum.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "improvement_momentum.html",
            error="Student ID must be an integer."
        )

    result = analyze_improvement_momentum(student_id)

    return render_template(
        "improvement_momentum.html",
        result=result,
        student_id=student_id
    ) 


@app.route("/academic-intelligence/subject-comovement")
def subject_comovement():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "subject_comovement.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "subject_comovement.html",
            error="Student ID must be an integer."
        )

    result = analyze_subject_comovement(student_id)

    return render_template(
        "subject_comovement.html",
        result=result,
        student_id=student_id
    ) 
@app.route("/academic-intelligence/exam-context")
def exam_context():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "exam_context.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "exam_context.html",
            error="Student ID must be an integer."
        )

    datasets = get_all_datasets()

    result = None

    exam_name = request.args.get("exam_name")

    if exam_name:
        result = analyze_exam_context(
            student_id,
            exam_name
        )

    return render_template(
        "exam_context.html",
        student_id=student_id,
        datasets=datasets,
        result=result
    ) 


@app.route("/academic-intelligence/cohort")
def cohort_performance():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "cohort_performance.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "cohort_performance.html",
            error="Student ID must be an integer."
        )

    datasets = get_all_datasets()

    exam_name = request.args.get("exam_name")

    result = None

    if exam_name:
        result = analyze_cohort_performance(
            student_id,
            exam_name
        )

    return render_template(
        "cohort_performance.html",
        student_id=student_id,
        datasets=datasets,
        result=result
    ) 


@app.route("/academic-intelligence/subject-consistency")
def subject_consistency():

    student_id = request.args.get("student_id")

    if not student_id:
        return render_template(
            "subject_consistency.html",
            error="Student ID is required."
        )

    try:
        student_id = int(student_id)
    except ValueError:
        return render_template(
            "subject_consistency.html",
            error="Student ID must be an integer."
        )

    result = analyze_subject_consistency(student_id)

    return render_template(
        "subject_consistency.html",
        result=result,
        student_id=student_id
    ) 





if __name__ == "__main__":
    app.run(debug=True)       

