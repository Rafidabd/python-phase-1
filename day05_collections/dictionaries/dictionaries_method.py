x={(1,2): "rafid" ,
   "nayan":{"Math":"100","English":99 },
   2095:"I wont live at that time",
   "y":[1,2,3]


}
 
#1-values:
print(x.values())


#2-keys:
print(x.keys())


#3-items:
print(x.items())

#4-get:
print(x.get("nayan"))


#5.pop:
y=x.pop("nayan")  ##removing corresponding everything
### here y will be equal to the values of nayan,and nayan will be removed
x.pop() 

#6.update:
x.update({(1,2):"Masfi",2095:"I will live"})   ###updating the value




#7.del:
del x["y"]   ##this will delete
print(len(x))

# 8.clear: 
x.clear()  


#9.set default:


print(x.setdefault(999,"?????"))   




####Get vs normal indexing:






#:
print(x.get("Nayaaaan"))  #this will return none
print(x["Nayaaaan"])  ##this will show error





