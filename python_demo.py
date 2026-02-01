# print("Hello World")

# colour=input("Enter a colour: ")
# plural_noun=input("Enter a plural noun: ")
# celebrity=input("Enter a celebrity: ")

# print("Roses are " + colour)
# print(plural_noun + " are blue")
# print("I love " + celebrity)

#----------------------------------------

# num1=float(input("Enter a number: "))
# num2=float(input("Enter another number: "))

# result=num1+num2

# print("The result is " + str(result))


#-----------------------------------------

#side = int(input("The side length in mm: " ))
#area = side**2

#print("The area of square in sq.mm: ",side**2)

#----------------------------------------------

# mov1=input("Enter the movie name: ")
# mov2=input("Enter the movie name: ")
# mov3=input("Enter the movie name: ")

# movies=[mov1,mov2,mov3]
# print(movies)

#----------------------------------------------

# num=[1,2,3,2,2]


# num_reverse=num.copy()
# num_reverse.reverse()


# if(num==num_reverse):
# 	print("List data is pallindrome")
# else:
# 	print("List data is not pallindrome")

#-----------------------------------------------

# movies=[]
# movies.append(input("Enter movie name: "))
# movies.append(input("Enter movie name: "))
# movies.append(input("Enter movie name: "))

# movies_reverse=movies.copy()
# movies_reverse.reverse()

# if(movies==movies_reverse):
# 	print("List data is pallindrome")
# else:
# 	print("List data is not pallindrome")

# print(movies)

#-----------------------------------------------


# grades=["B","A","D","C","F","A"]
# grades.sort() # This will sort the list in place but will not return a new list and return None
# grade_sort=sorted(grades) # This will sort the list and return a new list
# print(grade_sort)


#-----------------------------------------------

# dict={
#     	"name":"John",
# 	"age": 23,
# 	"Gender" : "Male",
# 	"Subjects" : ["Maths", "Science"]
# }

# print(dict)
# print(dict["name"]) # This will print the value of the key "name"
# dict["name"]="Sena" # This will update the value of the key "name"
# print(dict)


#-----------------------------------------------

# Marks={} # This is a dictionary
# Marks["Maths"]=input("Marks of Maths :")
# Marks["Science"]=input("Marks of Science :")
# Marks["English"]=input("Marks of English :")

# print(Marks)

#-----------------------------------------------

# numbers={9,"9.0"}
# print(numbers)

#-----------------------------------------------

# i=1
# while i<=100:
# 	print(i)
# 	i+=1    


#-----------------------------------------------

# i=1
# while i<=100:
# 	print(i)
# 	i+=1    

#-----------------------------------------------

# number=input("Print table for number: ")

# i = 1
# while i <= 10:
#     print(int(number) * i)
#     i += 1

#-----------------------------------------------

# num = [12,73,33,14,6,8,55,35,36,98]    

# i=0
# while i<=len(num)-1:
#     print("Number at:",i,num[i])
#     if (num[i]==33):
#         print("The number is 33")

#     else:
#         print("The number is not 33")

#     i+=1
# print("Loop Ended")    # Indentation is important solution

#------------------------------------------------

# i=0
# while i<=10:
#     print(i)
#     if(i==3):
#         break
#     i+=1

#------------------------------------------------

# i=0
# while i<=10:
    
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#-------------------------------------------------

# nums = (12,14,56,64,3,21,35)

# for val in nums:
#     if(val==56):
#         print("The number 56 found")
#         break
#     else:
#         print("The number 56 not found")
# print("Loop end")      

#--------------------------------------------------

# for i in range(100, 0, -1): #100 - Start, 0= Stop, -1=Range
#     print(i)

#--------------------------------------------------

# def add_num(a=3, b=4): #This is function in python
#     print(a+b)

# add_num()

#--------------------------------------------------

#Recursion Function
# def print_num(n):
#     if(n==0):   #Base case to stop recursion loop
#         return
#     print(n)
#     print_num(n-1)


# print_num(10)

#---------------------------------------------------

# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return fact(n-1)*n

# print(fact(6))

#----------------------------------------------------

# def natural_num(n):
#     if(n==0):
#         return 0
#     return natural_num(n-1)+n # Call same function with some chnages so loop continues

# sum=natural_num(5)    
# print(sum)

# class Student():
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val  
#             avg=sum/3
#         print(avg)    

# s=Student("groot",[90,92,95])
# s.get_avg()

#----------------------------------------------------

class Account():
    def __init__(self, account_no, balance):
        self.balance=balance
        self.account_no=account_no

    def debit(self, debit_amount):
        self.debit_amount = debit_amount
        self.balance =self.balance - self.debit_amount
        print("Debit balance", self.balance)

    def credit(self, credit_amount):
        self.credit_amount = credit_amount
        self.balance=self.balance + self.credit_amount
        print("Credit balance",self.balance)

holder = Account(12345, 100000)
holder.debit(20000)
holder.credit(30000)

