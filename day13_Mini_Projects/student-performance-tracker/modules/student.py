from modules.storage import load_data,save_data

def add_student(student_id,name,marks):
    data=load_data()
    data[student_id]={"name":name,"marks":marks}
    save_data(data)

def view_student(student_id):
    data=load_data
    return data.get(student_id)



