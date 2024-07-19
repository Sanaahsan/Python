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

