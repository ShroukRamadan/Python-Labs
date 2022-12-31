

########################################################

'''
volwels=["a","e","i","o","u"]
str=input("Enter your string: ")
count=0
for char in str:
   if char in volwels:
    count+=1

print(count)

'''

###################################################

'''
ls=[]
size=int(input("Enter size of your list: "))

for i in range(0,size):
    ele=input("Enter elements: ")
    if not ele.isdigit():
        ele=input("plese enter number: ")
    ls.append(int(ele))  

print(ls)

ls.sort()
print("Sort Ascending5: ", ls)
ls.reverse()
print("Sort Descending: ",ls) 


'''

#############################################################3


'''

str=input("Enter your string: ")

count=0
for i in range(0,len(str)-2):
    if str[i] == "i" and str[i+1]=="t" and str[i+2]=="i":
         count+=1



print(count)

'''

  
#########################################################################################

'''

volwels=["a","e","i","o","u"]
str=input("Enter your string: ")
new_str=""
for char in str:
   if char not in volwels:
    new_str+=char

print(new_str)

'''

########################################################################################


'''
str=input("Enter your string: ")
count=0
for i in range(0,len(str)):
    if str[i] == "i":
        count=i+1
        print(count)

'''
  

#######################################################################
'''

num=int(input("Enter The Number: "))
ls1=[]
ls2=[]
for i in range(1,num+1):
    for j in range(1,i+1):
        ls1.append(i*j)
    ls2.append(ls1)
    ls1=[]
print(ls2)

'''

#########################################################################

'''
height = int(input("Enter Height of Pyramid: "))
for i in range(height):
	print (" "*(height-(i+1))+("*"*(i+1)))
'''
##########################################################################

