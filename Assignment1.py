# WAP to accept the electricity unit consumption and calculate total price at the rate of 5rs per unit. Give a discount of 10% on over all bill.

n=int(input("Type your electricity unit consumption:"));
unit=n*5;
Discount= unit*0.10;
Bill=unit-Discount;
print(Bill);


# WAP to accept marks of 5 subjects and find total marks and % assuming full marks as 100 in each subject.

Maths=int(input("Enter Maths marks:"));
English=int(input("Enter English marks:"));
Physics=int(input("Enter Physics marks:"));
Biology=int(input("Enter Biology marks:"));
Computer=int(input("Enter Computer marks:"));
Total=Maths+English+Physics+Biology+Computer;

Percentage= Total/500*100;
print(Percentage);



# WAP to swap values of two numbers

# 1.Using 3rd varibale

a=10;
b=5;
temp=a;
a=b;
b=temp;
print("a=",a,"b=",b);

# 2. Without using 3rd varibale

a=10;
b=5;
a=a+b;
b=a-b;
a=a-b;
print("a=",a,"b=",b);


# WAP to accept total sales amount and find profit amount @5%

# WAP to check whether an 'age' is eligible for voting or not

age=int(input("Enter your age"));
if age>=18:
    print("Eligible");
else:
    print("Not eligible");



# WAP to find max between two numbers

a=int(input("Enter 1st number:"));
b=int(input("Enter 2nd number:"));
if a>b:
    print("a is greater than b");
else:
    print("b is greater than a");


# WAP to check whether a given number is positive, negative or 0

a=float(input("Enter your number"));
if a>0:
    print("Positive");
elif a<0:
    print("Negative");
else:
    print("Zero");

# WAP to find the middle number


