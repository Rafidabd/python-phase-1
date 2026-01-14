def rafid_func():
    print("Hello.This is rafid abdullah") ##if we call this function,this will happen
#####now we have set up our function


rafid_func() ###calling the function



####returning something:

def rafid_func () :
    return 'hello rafid.'

print(rafid_func())  ####this will return as string

print(len('test'))  ####will return 4





##arguements and parametres:


def porte_bosh(name,age):  ###parametre set 
    print("ei shala tor syllabus sesh hoise?")
    print(f"{name},porte bosh vai.")
    print(f"everyone expects a lot from you..your  age is {age}")

porte_bosh("rafid","19") ###arguements passed..******Order matters
porte_bosh("Masfi","18")

porte_bosh(age="19",name="rafid")   ####order doesnt matter that way



#######Returning in function:

#return basically means . 1)the function will do its work and end 2) then it will transform into what we have wanted
##basically think of it as the function being turned into something





def add (x,y) :
    z=x+y
    return z
def sub (x,y) :
    z=x-y
    return z
def mul (x,y) :
    z=x*y
    return z
def div (x,y) :
    z=x/y
    return z


print(add(1,2))  ##basically means print(3)
print(sub(1,2))
print(mul(1,2))
print(div(1,2))




#####*args and **kwargs:

#allows us to have random number of arguements when we dont know how much we should input


#If you do not know how many arguments will be passed into your function, add a * before the parameter name.


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")















