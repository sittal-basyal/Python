string =input("Enter a string: ")
def palindrome(string):
 if((string[::-1])==string):
    return("is palindrome")
 else:
    return("is not palindrome")
print(f"The string {string} {palindrome(string)}")
