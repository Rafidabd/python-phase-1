"""
TYPES OF ERRORS IN PYTHON

1. Syntax Error
   - Wrong syntax
   - Spelling mistakes
   - Detected before execution

2. Logical Error
   - Syntax is correct
   - Logic is wrong
   - Program runs but gives wrong output

3. Runtime Error
   - Occurs during execution
   - Example: division by zero, file not found
"""

# GENERAL FORMAT OF EXCEPTION HANDLING

"""
try:
    # code that may cause error
except ExceptionType:
    # runs if error occurs
else:
    # runs if no error occurs
finally:
    # always runs
"""

try:
    f=open("day08_file_handling/sample.txt") 
   
    ##file doesnt exist.so if we run the code,it will throw an error
    # var_not_defined=var
except FileNotFoundError:
    print("sorry this file doesnt exist") 


except Exception as x:
    print(x)  ##this will print out the exact error
else:
    print(f.read())
    f.close()
finally:
    print("executing the code at last....")  ##regardless if the code is succesful or not,it will run 




##Raising exception on our own:

try:
    f=open("day08_file_handling/sample2.txt")
    if f.name=="day08_file_handling/sample2.txt":
        raise Exception    ####Even if there's no error..we can raise custom errors on our own

except Exception:
    print("no,this file cant be opened by you") 
except FileNotFoundError as x:    
    print(x)
else:
    print(f.read())
finally:
    print("executing the code finally...")



##Math operation:

try:
    a = int(input("Enter a number: "))
    result = 10 / a
except ValueError:
    print("Input must be a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Done")







