num=int(input("Enter a number: "))

def factorial(num):
 fact=1;
 if(num==0):
   return 1;
 else:
  for i in range(1,num+1):
    fact=fact*i
 return fact;

print(f"Factorial of {num} is {factorial(num)}")
