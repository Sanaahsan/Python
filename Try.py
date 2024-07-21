# WAP to find products of digits of a given number

num=int(input("Enter your number"))
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