#using format:
first_name="Rafid"
last_name="Abdullah"

sentence="my name is {} {}".format(first_name,last_name)
# usage of f string:
sentence_2=f"my name is {first_name.upper()} {last_name.lower()}"

print(sentence)
print(sentence_2)


#Printing from a dictionary:

Data={'Name':'Rafid',
      'age':'19',
      'roll':12611052}


sentence_3="My name is {}.I am {} years old.My roll is {}".format(Data['Name'],Data['age'],Data['roll'])
print(sentence_3)


sentence_3=f"My name is {Data['Name']}.I am {Data['age']} years old.My roll is {Data['roll']}"
print(sentence_3)


#Pads:

for x in range(1,11):
    print(f"the value is {x:02} ")  ##01,02,03..0 will be padded for 2 digit numbers



#precision:


var=9.928972

sent=f"variable is equal to {var:.4f}"  
#first 4 digits after the radix point.this will also have the floating value 

print(sent)


































