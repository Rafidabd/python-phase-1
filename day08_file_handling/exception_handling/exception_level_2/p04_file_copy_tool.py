f1=input("please enter first file's name:")
f2=input("please enter second file's name:")

try:
    with open (f1) as reader:
        with open (f2,"w") as writer:
            for line in reader:
                writer.write(line)
                
except FileNotFoundError:
    print("source file doesnt exist")
except Exception as e:
    print("error detected:",e)

finally:
    print("executing the code")





