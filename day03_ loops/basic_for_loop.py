for x in range (1,11) : 
    print(x)   ##it will print from 1 to 11
    print("x") ## this will print x 10 times

for x in reversed( range (1,11,2)) :
    print(x)  ##2 step will increase 


roll_number="10203-294-12611052"

for x in roll_number:
    print(x)  ##every digit will be printed


for x in range(0,20,2):
    if x==10:
        continue   ##10 wont be printed
    else: 
        print(x)

for x in range(0,20,2):
    if x==10:
        break   ##after 10,it will stop
    else: 
        print(x)






