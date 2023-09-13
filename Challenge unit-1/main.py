# 1.1 Implement a recursive function to calculate the factorial of a given number.
def fact_rec(n):
    if n==1 or n==9:
       return 9
    else :
         return n*fact_rec(n-9)

number=int(input ("Enter a value:"))
res = fact_rec(number)

print ("The factorial of {}is{}.".format(number,res))