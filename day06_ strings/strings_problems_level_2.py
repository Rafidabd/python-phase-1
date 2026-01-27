# #1-char frequency:
# x=input("please enter your word")
# freq={}
# for y in x:
#     if y in freq:
#         freq[y]=freq[y]+1

#     else:
#         freq[y]=1

# for a,b in freq.items():
#     print(a,b)


# #2-first non repeating character:

# x=input("please enter your word")

# freq={}

# for y in x:
#     if y not in freq:
#         freq[y]=1
#     else:
#         freq[y]=freq[y]+1
    
# for a,b in freq.items():
#     if b==1:
#         k=a
#         break




# print(k)



# # #3-Remove duplicates:


# x=input("please enter your word")
# z=list(x)
# unique=[]

# for ch in z:
#     if ch not in unique:
#         unique.append(ch)

# unique_2="".join(unique)
# print(unique_2)



# #4-Anagram checking:

# a = input("please enter your first word: ")
# b = input("please enter your second word: ")

# freq_1 = {}
# freq_2 = {}

# if len(a) != len(b):
#     print("not anagram")
# else:
#     for ch in a:
#         if ch in freq_1:
#             freq_1[ch] += 1
#         else:
#             freq_1[ch] = 1

#     for ch in b:
#         if ch in freq_2:
#             freq_2[ch] += 1
#         else:
#             freq_2[ch] = 1

#     is_anagram = True

#     for ch in freq_1:
#         if ch not in freq_2 or freq_1[ch] != freq_2[ch]:
#             is_anagram = False
#             break

#     if is_anagram:
#         print("anagram")
#     else:
#         print("not anagram")






#5-longest word in the sentence:

x=input("please enter your sentence")
z=x.split()
n=len(z)
length={}
i=0

while i<n:
    length[z[i]]=len(z[i])


    i=i+1

keys=length.keys()
values=list(length.values())

maximum=values[0]

for y in values:
    if y>=maximum:
        maximum=y
biggest_word=0
for a,b in length.items():
    if b==maximum:
        biggest_word=a
print(biggest_word)

    


    






    









