
# Plaindrome 525

n=int(input("Enter your number:"));
original=n;
rev=0;
while(n>0):
    rev=(rev*10)+n%10
    n=n//10;
if (original==rev):
    print("Yes");
else:
    print("No")    




