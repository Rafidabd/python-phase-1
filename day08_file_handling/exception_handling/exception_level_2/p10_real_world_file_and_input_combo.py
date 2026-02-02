x=input("please enter the name of the file:")
try:
    with open(x,"r") as Reader:
     with open("new_sum_file.txt","w") as Writer:
      for values in Reader:
        k=100/int(values)
        Writer.write(str(k)+"/n")
except ValueError:
  print("invalid values inside the file")
except ZeroDivisionError:
  print("zero cant be divided")
except FileNotFoundError:
  print("file doesnt exist")
except Exception as e:
  print(e)
  
        
        


    

    