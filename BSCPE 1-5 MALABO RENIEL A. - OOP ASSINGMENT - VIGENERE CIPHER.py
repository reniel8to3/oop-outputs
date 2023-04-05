#Name: Malabo, Reniel A.            #Program and Section: BSCPE 1-5
#Subject - Object Oriented Programming      #Problem 3 - VIGENERE CIPHER

#Write a program that asks the user for the plaintext (all uppercase letters,no spaces) and the keyword (all uppercase letters) and produce the cipher text using the Vigenère cipher. Give the output of your program for the following message and key: Message: THISISTHELASTTASKHOORDAY Key: KNIGHTS
#create a main function
def main():
#ask the user for their message and key.    
    print ('\033[1;35m Hello!  This program is designed to create a Vegenere Cipher.')
    import time
    time.sleep(1)
    plaintext = input("What do you want to decipher? Please use uppercase letters with no spaces only. ")
    keyword = input("What is the key to the code? Please use uppercase letters only. ")
    secret_code = encrypt(plaintext, keyword)
    secret_revealed = decrypt(secret_code, keyword)

    print('Deciphering...')
    import time
    time.sleep (2)
    print("The resulting Vigenere Cipher is: " + secret_code)
    import time
    time.sleep(1)
    print("Your code is : " + secret_revealed)
    import time
    time.sleep(1)

#create a dictionary.
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#create defining variables.
plaintext_to_index = dict(zip(letters, range(len(letters))))
index_to_plaintext = dict(zip(range(len(letters)), letters))

#create an encrypt function.
def encrypt(plaintext, keyword):
    encrypted = ""
    split_message = [plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (plaintext_to_index[letter] + plaintext_to_index[keyword[i]]) % len(letters)
            encrypted += index_to_plaintext[number]
            i += 1

    return encrypted

#define decrypt function
def decrypt(plaintext, keyword):
    decrypted = ""
    split_encrypted = [plaintext[i : i + len(keyword)] for i in range(0, len(plaintext), len(keyword))]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (plaintext_to_index[letter] - plaintext_to_index[keyword[i]]) % len(letters)
            decrypted += index_to_plaintext[number]
            i += 1

    return decrypted

main()