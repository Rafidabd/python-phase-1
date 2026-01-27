#1-reversing a string:

x=input("Please enter your word")
j=len(x)
rev=x[::-1]
print(rev)

#2-Vowel counter

x=input("please enter your word")
vowel=0
for y in x:
    if y=='a' or y=='e' or y=='i' or y=="o" or y=='u' or y=='A' or y=='E' or y=='I'or y=='O' or y=='U':
        vowel=vowel+1
print("total vowel number :",vowel)   


#3-Pallindrome:
x=input("please enter your word")
if x==x[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")


#4-Uppercase,lowercase counter:


x=input("please enter your word")

upp=0
low=0

for y in x:
    if y.isupper():
        upp=upp+1
    else:
        low=low+1
print(f"uppercase:{upp} and lowercase:{low}")



#5-Space remover:


x=input("please enter your sentence")

z=x.replace(" ","")
print(z)





