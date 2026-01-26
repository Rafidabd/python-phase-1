#dictionary= a collection 0f {key:value} pairs
#ordered and changeable ,no duplication


coins={"Bangladesh":"Taka","India":"rupee",
       "United states":"dollar"}

# print(dir(coins)) ####this will show all the method
# print(help(coins))

print(coins.get("Bangladesh")) ###getting a value
print(coins.get("Japan")) ###this will show none


coins.update({"UK":"Pound"})  ###updating the dictionary
coins.pop("India") ##removing india

print(coins)

coins.popitem()   ###this will remove the latest value

coins.clear()  ##this will clear it

keys=coins.keys()  ###this will provide only the keys
print(keys)



for key  in coins.keys():
    print(key)    ##iterating and printing them


values=coins.value()   ###this will provide the values

items=coins.items() ###this will provide all the items in a pair
print(items)

for key,value in coins.items():
    print(f"{key}:{value}")


    
#Nested dictionaries and indexing:


Marks={"Rafid":{"Math":"100","English":99 },"Nayan":{"Math":97,"English":100}}
print(Marks["Rafid"]["English"])   ###this will print english  mark of rafid


Marks["Rafid"]["English"]="100"  ###updating




###keys and values can be aything..keys  cant be list btw,but can be tuples


x={(1,2): "rafid" ,
   "nayan":{"Math":"100","English":99 },
   2095:"I wont live at that time",
   "y":[1,2,3]
}
 










