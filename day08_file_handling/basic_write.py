###-------###
"""
Note:Reading consumes data. Writing creates or modifies data.
Writing is destructive by default.
"""


with open ('day08_file_handling/sample2.txt','w') as f:
    pass #this will open a new file..if the file existed,it would overwrite it



with open ('day08_file_handling/sample2.txt','w') as f:
    f.write("this is the first line added") 
    f.write("this is the second line added") #it will add to where we left it
   ##Writing doesnt create newline by default \n must be added.

##A good approach of making new lines:
with open ('day08_file_handling/sample2.txt','w') as f:
 Lines=["First line\n","Second line\n","third line\n"]
 f.writelines(Lines)



#-----Safer:(Append):
with open ('day08_file_handling/sample2.txt','a') as f:
   f.write("So this is appending..it wont overwrite.")  ##automatically will reach the EOF and then add



#------Read and write method:
with open ('day08_file_handling/sample2.txt','r+') as f:
   print(f.read(5))
   f.write("writing will start where the pointer currently is")




##Overwriting with seek:
with open ('day08_file_handling/sample3.txt','w') as f:
   f.seek(2)
   f.write("EFGHJ")


   

#Line by line writing:
with open ('day08_file_handling/sample4.txt','w') as f:
   for i in range(1,10):
      f.write(f"this is line {i}\n")



#Read---Process---Write:*********

#purpose:Read–Process–Write exists so we can transform data without loading everything into memory.

#[ INPUT FILE ] ──▶ READ ──▶ PROCESS ──▶ WRITE ──▶ [ OUTPUT FILE ]

with open("day08_file_handling/sample.txt", "r") as reader:
    with open("day08_file_handling/sample5.txt", "w") as writer:
        for line in reader:
            
          writer.write(line.upper())


   
















