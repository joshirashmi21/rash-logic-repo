#program about checking if a string is a palindrome


string=input("Enter a string please: ")

i =0
j= len(string)-1

while (i<=j):
          if (string[i]==string[j-i]):
                    if(i==j):
                              print ("Input String is a palindrome")
                              break
          else:
                    print("Input String is not a palindrome")
                    break
          
          i=i+1
          
