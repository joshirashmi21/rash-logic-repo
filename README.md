# rash-logic-repo
#Program to display fibonacci series up to term provided by user
print("Program to display fibonacci series")
term=int(input("Enter the term upto which series should be displayed "))
if term <=0:
     print("This is not a valid number")
else:     
     N=1
     N1=0
     N2=0

     print(N)

     for counter in range (0,term-1):
          N2=N1
          N1=N
          N=N1+N2
          print(N)

value=input("Enter to exit")
