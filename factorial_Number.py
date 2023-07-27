#calculate the  factorial of a given number
#find the number of trailling zeros

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
        # result=1
        # for i in range(1,n+1):
        #     print(i)
        # return factorial
if __name__ =="__main__":
    n=int(input("enter number:\n"))
    fac=factorial(n)
    print(f"the factorial is:{fac}")
