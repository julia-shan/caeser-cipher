def encrypt(text, shift):

    cipher = ""

    for i in range(len(text)):
        char = text[i]

        if(char == " "):
            cipher += char
        elif(char.isupper()):
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:  
            cipher += chr((ord(char) + shift - 97) % 26 + 97) 

    return cipher
