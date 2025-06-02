userinput=(input("Enter any string")).lower();
def count_variable():
    count =0
    for i in range (0,len(userinput)):
     if userinput[i] in "aeiou":# e and i are always truthy in python
      count+=1;
    return count
print(f"Vowels has been used {count_variable()} times")
