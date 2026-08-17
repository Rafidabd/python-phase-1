from flask import Flask, render_template, abort
from flask import Flask, render_template, request, redirect, url_for
from modules.student_manager import get_all_students,get_student_by_id
from modules.dataset_manager import get_all_datasets,get_dataset_by_name,create_dataset,add_student_record
from modules.config_loader import load_config
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




if __name__ == "__main__":
    app.run(debug=True)      