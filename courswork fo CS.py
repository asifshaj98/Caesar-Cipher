#Introduction to the programme
print ("Welcome to my Programme")
print ("======================================================================")
# user has a choice of loading a file to encrypt or decrypt
print ("To open a file enter - enter 1 ")
print()
#User has a choice of entering there own message to be encrypted or decrypted
userinput = input("To enter your message - enter 2")
if  userinput=='1':
#If user chooses to open a file, the programm would ask for the file fil
    file = input("Please name your file")
    file = file + ".txt"
    fo = open (file, "r+")
    message = fo.read ();
    #The message will display the name of the the file 
    print ("The file ",file," contains the message = ",str(message)) 
    fo.close()
#If the user enters 2,they will be asked to enter their message
else:
    message = input('Enter Message')
#User has a choice of encrypting or decrypting    
def getMode():
    while True:
        print('Do you want to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
mode = getMode()
#Choose a key/Offset between the value 1-26
def getOffset():
    #key = int(input('Choose an offset, 1-26?'))
    #key = 0
    while True:
        print('Choose an offset,1-26')
        key = int(input())    
        if (key >= 1 and key <= 26):
            return key
        else:
            print("Please enter a offset between 1-26")
key = getOffset()
characters = 'abcdefghijklmnopqrstuvwxyz'
translated = ''
message = message.lower()
for symbol in message:
    if symbol in characters:
        num = characters.find(symbol)
        #if the user chooses to encrypt the message,the number will be added from the chosen offset
        if mode =='encrypt'or mode =='e':
            num = num + key
        #If the user chooses to decrypt the message,the number will be taken away from chosen offset
        elif mode =='decrypt'or mode =='d':
            num = num - key
        if num >= len(characters):
            num = num - len(characters)
        elif num < 0:
            num = num + len(characters)
        translated = translated + characters[num]
    else:
         translated = translated + symbol
#The programm displays the new translated meesage as "This is now translated as ..(message).."
print ("This is now translated as = ", translated)
#The user then has a choice of saving or rewriting the file with the new message
option = input("Do you wish to save the file with your message press y?")
if option =='y':
    filename = input("Enter a name for the file")
    #The file will be called anything that the user wishes to name it 
    f = open(filename + ".txt","w")
    f.write(str(translated))
    f.close()
    print ("Message Saved")
else:
    #The programm will display that the message has not been saved in to the file.
    print ("Message not saved in file")   

