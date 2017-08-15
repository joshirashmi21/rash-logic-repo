#Program to display fibonaci series using recursive functions

def fib(n):

    if(n<=1):
        return n    

    else:
        return (fib(n-1)+ fib(n-2))


print("Fibonacci sequence:")

#print("Enter the term upto which you want the sequence ")

n=int(input("Enter the term upto which you want the sequence"))

for i in range (n):
    value=fib(i)
    print (value)
    

      
