#Name: Malabo, Reniel A.            #Section: BSCPE 1-5
#Subject - Object Oriented Programming      #Problem 2 - DECRYPTION

#Write a Python Script that will accept a string as encrypted text and then the program will decrypt it using the following character substitute:'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !

#Ask user what message they want to decrypt.
print("\033[1;35m Th#s pr+gr*m #s m*de t+ d&crypt m&ss*g&s th*t s!bst#t!t&s th& ch*r*ct&rs '*' as 'a', '&' as 'e', '#' as 'i', '+' as 'o', and '!' as 'u'.")
import time
time.sleep(3)
print("\033[1;35m Hmmm... Somethings not right...")
import time
time.sleep(3)
print ("\033[1;35m OH MY BAD... Take 2...")
import time
time.sleep(3)
print("\033[1;35m This program is made to decrypt messages that substitutes the characters '*' as 'a', '&' as 'e', '#' as 'i', '+' as 'o', and '!' as 'u'.")

code_encrypted=input('What do you want to deciper? Type the message here: ')
code_decrypted=""
#The decryption parameters are as follows:
for i in range (len(code_encrypted)):
#if the character is '*', change it to 'a'
    if code_encrypted[i]=="*":
        code_decrypted +="a"
#if the character is '&', change it to 'e'  
    elif code_encrypted[i]=="&":
        code_decrypted +="e"
#if the character is '#', change it to 'i'  
    elif code_encrypted[i]=="#":
        code_decrypted +="i"
#if the character is '+', change it to 'o'  
    elif code_encrypted[i]=="+":
        code_decrypted +="o"
#if the character is '!', change it to 'u'  
    elif code_encrypted[i]=="!":
        code_decrypted +="u"
    else:
        code_decrypted+=code_encrypted[i]
#Time to check the results
print ("\033[0;33m Deciphering the code...")
import time
time.sleep(3)
print("\033[1;35m I've deciphered your code as", code_decrypted, '.')