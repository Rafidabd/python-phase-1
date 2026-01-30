# f=open("day08_file_handling/sample.txt", "r")
# content=f.read()
# print(content) 
# f.close() 

###professional and safest approach:
#using with,context manager:
# with open("day08_file_handling/sample.txt",'r') as f:
#     content=f.read()
#     print(content)
#     print(len(content))
#     #no need for close
# print(f.closed)  ##this will return true.as we are outside of it


#now if we get out of the with identation,it will automatically 


#Reading lines:
with open("day08_file_handling/sample.txt",'r') as f:
    # f_lines=f.readlines()  ##all the lines in a list
    print(f.readline())  ##pointer will be at 1st line,will print the 1st line
    print(f.readline())  ##now poInter wIll be at the 2nd line
    #but this will create spaces between by default,so:
    print(f.readline(),end="")

#looping on the file :
with open("day08_file_handling/sample.txt",'r') as f:
    for line in f:
        print(line,end="")   ##line by line

with open("day08_file_handling/sample.txt",'r') as f:

 print(f.read(100))   ##first 100 chars will be printed
 print(f.read(100)) #now it will pick out the rest of the chars.
 print(f.read(100)) #it will return an empty string..as there's nothing left



#Another method:
with open("day08_file_handling/sample.txt",'r') as f:
   size_to_read=5
   f_contents=f.read(size_to_read)
   print(f.tell())  #it will show the pointers position
#    while len(f_contents)>0:
#       print(f_contents,end="-")
#       f_contents=f.read(size_to_read)




#Seek method:
with open("day08_file_handling/sample.txt",'r') as f:
   size_to_read=5
   print(f.read(size_to_read))
   f.seek(0)
   print(f.read(size_to_read))  ##it will show the same output because we have reset the position of our pointer



   





















