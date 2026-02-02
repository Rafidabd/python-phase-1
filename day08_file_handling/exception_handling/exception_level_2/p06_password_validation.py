x=input("please enter your password:")
n=len(x)
contains_digit=x.isalpha()
try:
    if n<8 or contains_digit==True:
        raise Exception
except Exception:
    print("Invalid password")
else:
    print("Password saved.")


