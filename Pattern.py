# NESTED LOOP

# O/P
#  1234
#  1234
#  1234
#  1234

i=1
while(i<5):
    j=1
    while(j<5):
        print(j, end="")
        j=j+1
    print()    
    i=i+1

# *
# **
# ***
# ****
# *****

i=1
while(i<=5):
    j=1
    while(j<=i):
        print("*" , end="")
        j=j+1
    print()    
    i=i+1

# 1
# 22
# 333
# 4444
# 55555

i=1
while(i<=5):
    j=1
    while(j<=i):
        print(i, end="")
        j=j+1
    print()
    i=i+1

# 1
# 12
# 123
# 1234
# 12345    

i=1
while(i<=5):
    j=1
    while(j<=i):
        print(j, end="")
        j=j+1
    print()    
    i=i+1

#      *
#     **
#    ***
#   ****
#  *****

i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ",end="")
        b=b+1
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    print()    
    i=i+1    

#     *   
#    ***
#   *****
#  *******
# *********    
  
k=1
i=1
while(i<=5):
    b=1
    while(b<=5-i):
        print(" ", end="")
        b=b+1
    j=1
    while(j<=k):
        print("*",end="")
        j=j+1
    k=k+2
    print()
    i=i+1  ;

#     1
#    123
#   12345
#  1234567
# 123456789

k=1;
i=1;
while(i<=5):
    b=1
    while(b<=5-i):
      print(" ",end="")
      b=b+1
    j=1
    while(j<=k):
        print(j, end="")
        j=j+1
    k=k+2
    print()
    i=i+1      

#     1
#    333
#   55555
#  7777777
# 999999999     

k=1;
i=1;
while(i<=5):
    b=1
    while(b<=5-i):
      print(" ",end="")
      b=b+1
    j=1
    while(j<=k):
        print(k, end="")
        j=j+1
    k=k+2
    print()
    i=i+1  

#     1
#    222
#   33333
#  4444444
# 555555555   
k=1;
i=1;
while(i<=5):
    b=1
    while(b<=5-i):
      print(" ",end="")
      b=b+1
    j=1
    while(j<=k):
        print(i, end="")
        j=j+1
    k=k+2
    print()
    i=i+1                   


    


      
