names=["rafid","Masfi","abdullah"]  ####list of strings
print(names[2]) ##index starts from 0,so it will print abdullah

matrix=[[1,2],["rafid","abdullah"]]  ##list inside list

mul=["rafid"]*100 ##### it wil be printed 100 times
print(mul)


x= names + mul ###strings can be added too


numbers=list(range(20))  ### with that we can also have numbers from 0 to 19

chars=list("hello world")
print(chars)   #####every characters will be listed individually 






##########Different operations on list:


lst=["a","e","f","g","h"]

print(lst[0])   #first item from the beginning (a)


print (lst[-1])  ###it will print the first item from the end (h)

lst[2] = "F"   ###modified

print(lst[0:3]) ##this will print the item from that range,first 3 item


print(lst[::2])  ##this is called step..that means 0,2,4,6....

print(lst[::-1]) ##reversed list will be printed




###List Unpacking:


numbers=[1,2,3,45,7,3,4,22,55,1]
a,b,c,d,e,f,g,h,i,j=numbers   ####every variable will have the same value accordingly

a,b,*other=numbers ###a,b will be seperated and others will be enlisted in a different list

first,*other,last=numbers ###in that case,first and last will be seperated













