def Addition(No1 , No2):
    print("Inside Addition Function")
    Ans =  0
    Ans =  No1 + No2 
    return Ans

def main():
    print("Inside main Function")
    print ("Enter the first number : ")
    A = int (input())

    print("Enter second Number : ")
    B = int (input())

    Result = Addition (A, B)

    print("Addition is : ", Result)

main()
print("End of applicaiton")