str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
c = 0

if (len(str1) == len(str2)):
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            c = c + 1
    print("Hamming distance is " + str(c))
else:
    print("Lengths are not equal")
