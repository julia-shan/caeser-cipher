def encrypt(text, shift):

    cipher = ""

    for i in range(len(text)):
        char = text[i]

        if(char == " "):
            cipher += char
        elif(char.isupper()):
            cipher += chr(ord(char) + shift)
        else:  
            cipher += chr(ord(char) + shift)

    return cipher
