#1-Printing dictionary:

fav_foods={"Rafid":"Chicken",
           "Masfi":"Beef",
           "Kazim":"Mutton",
           1:"biriyani",
           2:[1,2,3]



           }

print(fav_foods)





#2-Count total number of pairs:


fav_foods={"Rafid":"Chicken",
           "Masfi":"Beef",
           "Kazim":"Mutton",
           1:"biriyani",
           2:[1,2,3]
}




keys=fav_foods.keys()
i=0

for x in keys:
    i=i+1

print("total pairs:",i)





#Search a key:


fav_foods={"Rafid":"Chicken",
           "Masfi":"Beef",
           "Kazim":"Mutton",
           1:"biriyani",
           2:[1,2,3]
}


x=input("please enter your key")
if x.isdigit():
    x=int(x)
if x in fav_foods:
    print(fav_foods[x])

else:
    print("key not found")



