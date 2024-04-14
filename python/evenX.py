def CheckEven(No):
    if(No % 2 == 0 ):
        print("It is a even number")
    else:
        print("It is a odd number") 

def main():
    print("Enter Number : ")
    A = int(input())
    
    CheckEven(A)

#Starter
if __name__ == "__main__":
  main()