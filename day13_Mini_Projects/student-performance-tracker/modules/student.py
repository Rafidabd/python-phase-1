from modules.storage import load_data,save_data

def add_student(student_id,name,section,physics,math,english):
    data=load_data()
    data[student_id]={"name":name,"section":section,"marks":{"Physics":physics,"Math":math,"English":english}}
    save_data(data)

def view_student(student_id):
    data=load_data()
    return data.get(student_id,"Student not found") 



