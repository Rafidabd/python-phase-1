Name="Hasnin Jahan Masfi"
Number="019139290"
x="hasninjahanmasfi"
y="23@23@45@98Q@9@"
p="       Spacious    "
#1-len:
print(len(Name))  #number of chars
#2-Find:
print(Name.find("Hasnin"))   #First occurance (index numb)
print(Name.rfind("a"))    #last occurance
print(Name.find("Q")) ##this will return -1
#3-capitalize:
print(Name.capitalize())  #this will capitalize only the first letter
#4-upper:
print(Name.upper())   #all characters will be of uppercase
#5-lower:
print(Name.lower())   #all characters will be of lowercase
#6-isdigit:
print(Name.isdigit())  #if all the chars are digit,this will return true,else false
print(Number.isdigit()) #this will return true

#7-isalpha:
print(Name.isalpha())   ##this will return false,because of space
print(Number.isalpha())
print(x.isalpha()) #this will return true,as theres no space

#8-count:
print(Number.count("0"))  #occurance of zero,this will return a value

#9-replace:

Z=y.replace("@","*")   ##y wont change ,thats why we gotta asign it to a new variable
print(Z)


#10-strip:
print(p.strip()) #this will remove all the spaces.leading and trailing
q="www.rafid.com"
print(q.strip("cmow.")) #it will print rafid only

#11-split:
print(Name.split())  #this will return a list of the strings,individually

#12-Join:
list_of_strings=['I','Love','You']
s="#".join(list_of_strings)
print(s)

#13,14-is lower,is upper:

print("RAFID ABDULLAH".isupper())  #True
print("rafid abdullah".islower())  #True as well


#14,15-starts with,ends with:

print("I am Rafid".startswith("I"))  #this will return true
print("I am Masfi".endswith("fi")) #this will return true as well


#16-partition:

sentence="Rfid is a good person"
parts=sentence.partition("a")  ##this will return a tuple with the elements being seperated,as a will be in middle
print(parts)



#additions of strings:
x="RAFID"
y="Abdullah"
z=x+y
print(z)  ##we wont have space here

z1=x+ "," +y

print(z1)  ##this will have space..but hard to keep track




