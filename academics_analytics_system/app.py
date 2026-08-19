from flask import Flask, render_template, abort
from flask import Flask, render_template, request, redirect, url_for
from modules.student_manager import get_all_students,get_student_by_id,get_student_record_from_dataset
from modules.dataset_manager import get_all_datasets,get_dataset_by_name,create_dataset,add_student_record
from modules.config_loader import load_config
from modules.analytics import (
rank_students,get_topper,get_lowest_performer,get_weak_students,get_dataset_statistics,
get_subject_averages,get_strongest_subject_overall,get_weakest_subject_overall,evaluate_student_record
)
from modules.predictor import get_student_academic_history, build_student_performance_series,analyze_student_trend,analyze_student_risk,predict_student_performance
from modules.insights import generate_student_insights


app = Flask(__name__)


@app.route("/")
def home():
    students = get_all_students()

    return render_template(
        "index.html",
        students=students
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

    return render_template(
        "analytics_dataset.html",
        dataset=dataset
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

if __name__ == "__main__":
    app.run(debug=True)       