# 1- very First python program
print("Hello World")

# 2- Program to take the average of two variables (Variables and Data types)
a=3
b=3
avg= a+b/2
print('Average of a and b is:',avg)

# 3- Take a number and convert it's type from int to string
z= 100
print(type(z)) 
y= str(z)
print(type(y)) 

# 4- Take a number from user as an input and check it's type
x=input('Enter a number :')
print("As we can see number entered by user is string type:", type(x))

# 5- Take a string and perform a simple slice function on it
str= "Jibran"
print(str[:6])
print(str[0:6:4]) 
# it will skip one member less than the last number in
# this case we use 4 in last place so 3 members will be skipped
print(len(str))

# 6- Convert first letter of string to upper case
low= "string"
x1=low.capitalize()
print(x1)

# 7- Update the dictionary by adding another item to it
dic= {'name':'Jibran',
      'Roll No':'033'
}
dic.update({'Depart':"CS"})
print(dic)

# 8-Make program using if else to if a person is valid for driving
age= input("Enter your age: ")
validAge= int(age)
if(validAge>=20):
    print("You can drive the car")
else:
    print("You are not eligible to drive the car")






