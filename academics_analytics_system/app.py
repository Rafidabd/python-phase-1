from flask import Flask, render_template, abort
from modules.student_manager import get_all_students,get_student_by_id

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


if __name__ == "__main__":
    app.run(debug=True)      