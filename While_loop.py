# LEVEL 1

# WAP tp print from 1 to 10

i=1
while(i<=10):
     print(i)
     i=i+1;

 # WAP to print from 1 to n
n=int(input("Enter your number:"));
i=1
while(i<=n):
    print(i)
    i=i+1

# # WAP to print from 10 to 1
i=10
while (i>=1):
    print(i)
    i=i-1

# # WAP to print from n to 1

n=int(input("Enter your number:"));
while(n>=1):
    print(n)
    n=n-1

# WAP to find sum from 1 to n

n=int(input("Enter your number"));
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1;
print(sum);

# WAP to print sum of square from 1 to n

n=int(input("Enter your number:"));
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1;
print(sum);

# WAP to print sum of cube from 1 to n

n=int(input("Enter your number:"));
i=1
sum=0
while(i<=n):
    sum=sum+(i*i*i)
    i=i+1;
print(sum);

# WAP to print only even numbers between 1 to n

n=int(input("Enter your number:"));
i=1
while(i<=n):
    if(i%2==0):
        print(i)
    i=i+1;
  

# WAP to find sum of first even numbers from 1 to n

n=int(input("Enter your number:"));
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1;
print(sum);

    
    
    

# WAP to find sum of first n even numbers.
n=int(input("Enter your number:"));
i=1
sum=0
count=0
while(count<n):
    if(i%2==0):
        sum=sum+i
        count=count+1
    i=i+1;
print(sum) ;   

    



# LEVEL 2

# WAP to find sum of digits of a given number
i=int(input("Enter your number"));
sum=0
while(i>0):
    sum=sum+(i%10)
    i=i//10;
print(sum)

# WAP to find sum of square of digits of a given number
i=int(input("Enter your number:"));
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10;
print(sum);

# WAP to find sum of cube of digits of a given number
i=int(input("Enter your number:"));
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10;
print(sum);

# WAP to check whether a given number is armstrong or not

i=int(input("Enter your number:"));
sum=0
count=i
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i//10;
if(count==sum):
    print("Yes,It is an ARMSTRONG number")
else:
    print("No")    


# WAP to find products of digits of a given number
n=int(input("Enter your number:"));
product=1
while(n>0):
    product=product*(n%10)
    n//10;
print(product);


# WAP to find sum of even digits and product of odd digits of a given number.

num=int(input("Enter your number: "))
sum=0
product=1
while(num>0):
    digit=num%10
    if(digit%2==0):
        sum=sum+digit
    else:
        product=product*digit
    num=num//10;
print(sum);
print(product)        

# WAP to reverse a given number
i=int(input("Enter your number:"));
rev=0;
while(i>0):
    rev=(rev*10)+i%10
    i//10;
print(rev);
    

# WAP to check whether a given number is a palindrome or not
n=int(input("Enter your number:"));
original=n;
rev=0;
while(n>0):
    rev=(rev*10)+ n%10
    n=n//10;
if(original==rev):
    print("Yes, it is a palindrome")
else:
    print("No,it's not a palindrome")    



# WAP to check whether a given number is pime or not
n=int(input("Enter your number:"))
i=1;
count=0;
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1;
if(count==2):
    print("It is a prime number")
else:
    print("It is not a prime number")        



# WAP to print factorial of a given number
i=int(input("Enter your number:"))
fac=1
while(i>0):
    fac=fac*i
    i=i+1;
print(fac)


# WAP to print fibonacci series upto a given number

n=int(input("Enter your number:"))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y


