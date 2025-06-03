# Write a function that returns the sum of all elements in a list of numbers.
num=int(input("Enter number of elements: "))
my_list=[]
for i in range(num):
    new_element=int(input(f"ENter list element {i+1} : "));
    my_list.append(new_element)
def sum_of_list(my_list):
 sum=0
 for i in my_list:
    sum=sum+i
 return sum;
print(f"The sum of list elements is {sum_of_list(my_list)}")
