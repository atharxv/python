from marvellous import Addition 
from marvellous import Multiplication
#we have imported specific functions.

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = Addition(A, B)
    print("Addition is : ", Ans)
    
    Ans = Multiplication(A, B)
    print("Multiplication is : ", Ans)

main()
