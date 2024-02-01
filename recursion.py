# Print first n Natural numbers
def PrintN(n):
    if n>0:
     PrintN(n-1)
     print(n,end="  ")

#PrintN(10)

# Print first n Natural numbers in reverse
def PrintreverseN(n):
    if n>0:
     print(n,end="  ")
     PrintreverseN(n-1)

#PrintreverseN(10)

#print first n odd natural numbers
def PrintoddN(n):
    if n>0:
        PrintoddN(n-1)
        print(2*n-1,end=" ")

#PrintoddN(10)


#print first n even natural numbers
def PrintevenN(n):
    if n>0:
        PrintevenN(n-1)
        print(2*n,end=" ")

#PrintevenN(10)


#print first n odd natural numbers in reverse order
def PrintoddNreverse(n):
    if n>0:
        print(2 * n - 1, end=" ")
        PrintoddNreverse(n-1)


#PrintoddNreverse(10)


#print first n even natural numbers in reverse
def PrintevenNreverse(n):
    if n>0:
        print(2 * n, end=" ")
        PrintevenNreverse(n-1)

#PrintevenNreverse(10)
print("uncomment the print statements to see the output")

#sum of first n natural numbers

def sumN(n):
    if n==0:
        return 0
    return n+sumN(n-1)

#print(sumN(0))

#Sum of first odd natural numbers

def sumOddN(n):
    if n==1:
        return 1
    return (2*n-1)+sumOddN(n-1)


#print(sumOddN(4))

#Sum of n even natural numbers
def sumEvenN(n):
    if n==1:
        return 2
    return (2*n)+sumEvenN(n-1)


#print(sumEvenN(4))

#Factorial of N natural numbers
def factN(n):
    if n==0:
        return 1
    return n*factN(n-1)

#print(factN(17))


#Sum of square of first N natural Numbers
def sumSqN(n):
    if n==1:
        return 1
    return (n*n)+sumSqN(n-1)

print(sumSqN(5))
