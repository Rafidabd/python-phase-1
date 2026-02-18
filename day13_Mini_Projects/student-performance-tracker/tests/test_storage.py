from  modules.storage import load_data,save_data
data=load_data()
print("loaded:",data)
data["students"].append({"name":"test student"})
print("saved")
