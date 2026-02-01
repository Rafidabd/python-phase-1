#collection which is ordered and unchangeable,used to group together related data

Student=("rafid",21,"Male")
x=("B",)  ###commas must be there for tuple with one element

y=(1,2,3,("rafid",2,"Nayan",("arab",5,6)))   ###nested tuple

print(Student.count("rafid"))   ##how many times it appears
print(Student.index("Male"))    ##shows the index number

print(y[3][3][1])    ###thats how we access the value 5 in it 

for x in Student:  ##3accesing with loops
    print(x)


####Tuples are imutable:

 # y[1]="B"    ###we might think that this will change..but it wont


 

