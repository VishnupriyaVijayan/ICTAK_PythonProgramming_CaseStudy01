#!/usr/bin/env python
# coding: utf-8
1). A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
# In[1]:


mark=float(input("Enter mark: "))
if mark>=80:
    print("Your Grade is A")
elif mark>=60:
    print("Your Grade is B")
elif mark>=50:
    print("Your Grade is C")
elif mark>=45:
    print("Your Grade is D")
elif mark>=25:
    print("Your Grade is E")
elif mark>=0:
    print("Your Grade is F")
else:
    print("Unidentified ")

2). You have a list of names. Create a new list which contains only the names with non-repeating characters.
Sample input = ['John','Peter','Meera','Mini','Krishna']
Sample output = [‘John’,Krishna]
# In[2]:


from collections import Counter

Sample_output=[]
flag=0

Sample_input = ['John','Peter','Meera','Mini','Krishna']

for name in Sample_input:
    count = list(Counter(name).values())
    flag=True if all(k==1 for k in count) else False
    print(name, flag)
    if flag==True:
        Sample_output.append(name)
        
print('\n Strings with non-repeated characters: \n',Sample_output)    

3. Take values of length and breadth of a rectangle from user and check if it is square or not.

# In[3]:


a,b=[float(x) for x in input("Enter length and breadth(cm):  ").split(",")]
print("This is a square.") if a==b else print("This is not a square.")

4. A student will not be allowed to sit in exam if his/her attendance is less than 75%. 
Take following input from user 
Number of classes held 
Number of classes attended.
And print percentage of class attended 
Is student is allowed to sit in exam or not.
# In[4]:


n_class,n_att=[int(x) for x in input("Enter total number of classes and number of classes attended:  ").split(",")]
n_percent=n_att/n_class*100
if n_percent>=75:
    print("Attendance %: {}\n \033[1;32m You are eligible to take exam.".format(n_percent))
else:
    print("Attendance %: {}\n \033[1;36m Sorry you are not eligible to take exam.".format(n_percent)) 

5. Create a list by taking length of the list and elements of the list from user. 
Then find the sum of the elements of the list. Also create a new called even list 
which contains only even numbers from first list and odd list which contains 
odd numbers from the list.

Sample input:
Length of the list = 5
List1 = [2,6,3,1,5]

Sum = 17
Even_list=[2,6]
Odd_list=[3,1,5]
# In[5]:


n=int(input("Enter length of the list: "))
list_1=[]
even_list=[]
odd_list=[]
for k in range(n):
    a=int(input("Enter element: "))
    list_1.append(a)

even_list=[k for k in list_1 if k%2==0]
odd_list=[k for k in list_1 if k not in even_list]
print("List: ",list_1)
print("Sum: ",sum(list_1))
print("Even list: ",even_list)
print("Odd list: ",odd_list)

6. Create a sample chatbot for an ecommerce website.
# In[6]:


print(" \033[1;38m Good Morning...")
print('Welcome to the virtual book shop.')
print("Search for books in different 'Genre', 'Language', 'Author' and more..\n Enter Q to stop. ")
list_genre=['Classics','Science fiction','Mystery','Historical','Self help']
list_lan=['English','Malyalam']
while (1):
    
    x=input()
    
    x=x.lower()
    y=x.split()
    
    if x=='q':
        print("See you soon.")
        break
    elif len(y)==0:
        print("Enter your quiry")
    elif x=='genre':
        print(" \033[1;36m Check-out books on", list_genre,' https://vitualbookhub/genres')
    elif x=='language':  
        print(" \033[1;34m Check-out books on", list_lan[0],' https://vitualbookhub/bookenglish')
        print(" \033[1;34m Check-out books on", list_lan[1],' https://vitualbookhub/bookmalayalam')
    elif x=='author':
        print(" \033[1;32m Check-out list of books with authors on https://vitualbookhub/bookauthors")
    else:
        print(" \033[1;30m Check out more books on https://virtualbookhub/home")
        

7. Write a program to find the roots of a quadratic equation. 
Get the co-efficients of quadratic equation ax^2+bx+c and display whether the roots are real and equal or real and distinct or roots are imaginary. You have to find the roots and display it as well.
# In[7]:


root_1,root_2=0,0
print("\033[1m Roots of Quadratic Equation Calculator\033[0m")
a,b,c=[float(x) for x in input("Enter the coefficients a,b,c in ax^2+bx+c:  ").split(",")]

k1=b**2-4*a*c
root_1=(-1*b+k1**(1/2))/(2*a)
root_2=(-1*b-k1**(1/2))/(2*a)

if k1>=0:
    print("The roots are real")
if k1<0:
    print("The roots are imaginary")
if root_1==root_2:
    print("The roots are equal")
if root_1!=root_2:
    print("The roots are distinct")

print("roots of {}x^2 + {}x + {} are {:.2f} and {:.2f}".format(a,b,c,root_1,root_2))    
    

8. Given a range of first 10 numbers, write a Python program to iterate from start number to the end number 
and print the sum of the current number and previous number.

Sample input: 
1….10

Sample output:
Current Number 1 Previous Number 0 Sum: 1
Current Number 2 Previous Number 1 Sum: 3
Current Number 3 Previous Number 2 Sum: 5…
…….
Current Number 10 Previous Number 9 Sum: 19
# In[8]:


a,b=[int(x) for x in input("Enter the range: ").split(",")]
print("\033[1m {:<16} {:<16} {:<8} \033[0m".format('Current_number','Previous_number','Sum'))
for i in range(a,b+1):
    print(" {:<16} {:<16} {:<8}".format(i,i-1,2*i-1))
    

9. Write a Python program to find the prime numbers in a given range. Get the range from user and print prime numbers in that range.
# In[9]:


a,b=[int(x) for x in input("Enter the range: ").split(",")]
prime_num=[]

if (a==0 or a==1):
    a=2
    
for k in range(a,b+1):    
    n=int(k**(1/2))    
    for kk in range(2,n+1):        
        if k%kk==0:
            break
    else:
        prime_num.append(k)
        
print("The prime numbers between ",a," and ", b," are ", prime_num)        

10. Write a Python program to print Fibonacci series in a given range. Get the range from user and print fibonacci numbers in that range.

# In[11]:


low_a,high_b=[int(x) for x in input("Enter the range: ").split(",")]

f1,f2=0,1
s=0
list_fib=[]
ch=True

if low_a==0:
    low_a=1
    list_fib.append(0)
if low_a==1:
    low_a=1
    list_fib.append(1)
       
if low_a>high_b:
    low_a,high_b=high_b,low_a
while (ch):
    f3=f1+f2
    if f3>=low_a and f2<=low_a:
        n_current= f2 if f2==low_a else f3
        n_pre= f1 if n_current==f2 else f2
        ch=False
    else:
        f1,f2=f2,f3

list_fib.append(n_current)
while(True):
    s=n_pre+n_current
    if s>high_b:
        break
    list_fib.append(s)
    n_pre,n_current=n_current,s    
print("Fibonacci series in the range {} and {} is {}".format(low_a,high_b,list_fib))    
    
    
    


# In[ ]:




