#sets are-
#1.unordered 2.mutable 3.only unique values 4.no indexing

#Creation and empty sets:

set_1={1,2,3}
s=set([1,1,2,3,4])  ###this will get s={1,2,3,4}
empty_Set=set()##empty set
print(empty_Set)


##Acessing set:

##we cant do s[0]

for x in set_1:
    print(x)  ##qwe have to loop it



#SET OPERATIONS:


#1-Adding and updatinh

set_1.add(6)
print(set_1) 
set_1.update([4,8,10])


#2-remove and discard and pop

set_1.remove(2)
print(set_1)  ##if not found,programme will show error

set_1.discard(6)
print(set_1)  ##if not found,autmatically will show not found
set_1.pop()  


#3-Memberships:
if 6 in set_1:
    print("6 is a element")
else:
    print("not ")


#Set operations:


A={1,2,3,4,5,6}
B={2,3,5,6,7}
C={0,7,6}

P=A|B
print(P) ##addition

X=A&B
X1=A.intersection(B,C)
print(X1)
print(X) #intersection

Y=A-B
print(Y) #diff
Y2=A.difference(B,C)


Z=A^B

print(Z)  #3symmetric diff ,either but not both









