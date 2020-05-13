#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

#Nth = int(input("Enter a number and the fibonacci will create itself from that number: "))

#fibo = []
#print(fibo)
def fibonacci(n):
    a = 0
    b = 1
    for i in range(0 , n):
        temp = a 
        a = b 
        b = temp + b
    return a 

for c in range(0,15):
    print(fibonacci(c))
    
