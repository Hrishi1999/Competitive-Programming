str = input("Enter string: ")

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

if(str == reverse(str)):
    print("Palindrome")
else:
    print("Not a Palindrome")