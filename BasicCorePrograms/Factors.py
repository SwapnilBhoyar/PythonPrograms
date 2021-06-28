"""
@Author: Swapnil Bhoyar
@Date: 2021-06-27 18:34:00
@Last Modified By: Swapnil Bhoyar
@Last Modified Date: 2021-06-28 11:44:00
@Title: Computes the prime factorization of N using brute force
"""
number=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=number):
    k=0
    if(number%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
