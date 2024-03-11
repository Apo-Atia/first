#Author: Ahmed Attia Abouzaid
#Ass1 Task3 problem 4
print("Welcome to the message encryptor ^_^ ") 
#make function that encrypts user input message
def message_encryptor():
    print("Welcome to the message encryptor ^_^ ") 
    while True:
        message=input("please enter a message: ")
        encrypted_message="" #Inialize the encrypted_message so I can add characters to it
        for character in message:
            if character.isalpha():# Use built in function to check if it's alphabet letter or just space or symbols and Punctuation mark
                if character=="z":#make condition for small "z" as it's the last letter in alphabet to not shift it but return it to "a"
                   character="a"
                elif character=="Z":#make condition for capital "Z" as it's the last letter in alphabet to not shift it but return it to "A"
                   character="A"  
                else:   
                   character=chr(ord(character)+1) #Shift the letter to the next one
                encrypted_message+=character       
            else: #Ignore encrypring the numbers, spaces, symbols and Punctuation mark
                encrypted_message+=character   
        print(encrypted_message)

message_encryptor()
