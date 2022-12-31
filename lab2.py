#######################################################################################

'''
def increase_one(lenght,start):
    arr=[]
    arr.append(start)
    for i in range(1,lenght):
        start+=1
        arr.append(start)
    return arr;



print(fun(6,1))

'''

##################################################################################

'''

def fizzbuzz(num):
    if num%3 ==0 and num%5==0:
        return "FizzBuzz"
    elif num%3==0:
        return"Fizz"
    elif num%5==0:
        return"Buzz"
    else:
        return "Not divisable by 5 and 3"


print(fizzbuzz(5))
'''

##############################################################################################

'''
def rev_str(str):
    new_str=""
    for i in str:
        new_str = i + new_str

    return new_str


print(rev_str("shrouk"))

'''  
#-----------OR--------------

'''
def rev_str(str):
    return str[::-1]



print(rev_str("shrouk"))

'''

###########################################################################################

'''

def valid_name():
    while True:
        name= input('Enter your name : ')
        if name != '' and ( not name.isdigit()):
            print("Confirmed Name")
            break
        else:
            name=input("Please Enter your name agin : ")
            continue

            
    

valid_name()

'''

def valid_info():
    pass




############################################################################################3


'''

def longestAlphabet(str):
    longest = ""
    string = ""
    count = 0
    topCount = 0
    for i in range(len(str)-1):
        if(str[i] <= str[i + 1]):
            string +=str[i]
            counter = counter + 1
        if counter > topCounter:
            topCounter = counter
            counter = 0
            longest = string  
            string = ""
    print("Longest substring in alphabetical order is: " + longest)

longestAlphabet('abdulrahman')

'''

#-----------OR----------------------

'''

def longestSubString(str):
    string = ''
    longest = ''
    for i in range(len(str)):
        if (str[i] >= str[i-1]):
         string += str[i]
        else:
         string = str[i]
        if len(string) > len(longest):
         longest = string
    print("Longest substring in alphabetical order is: " + longest)


longestSubString('abdulrahman')


'''
##################################################################################3
'''

def read_num():   
    num=input("Enter number:")
    sum=num
    count=1
    avg=0   
    while num !="done": 
        num=int(num)
        if num.isdigit():
            num=int(input("Enter number:"))
        else:
            num=int(input("Please Enter number Not Charater:"))
    sum+=num
    count+=1       
        

    
    avg=sum/(count)
    print("total numbers= ",sum)
    print("count of numbers= ",count)
    print("avarage of numbers= ",avg)


read_num()

'''

##########################################################################################

def hangman():
    pass



##########################################################################################