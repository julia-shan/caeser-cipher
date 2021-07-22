def decrypt(text, shift):
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    possible_keys = []

    if shift != 0:
        decipher = " "  
        for letter in text:
            if(ord(letter) < 65 or ord(letter) > 122):
                decipher += letter
            elif(letter.isupper()):
                decipher += chr((ord(letter) - shift - 65) % 26 + 65)
            else:  
                decipher += chr((ord(letter) - shift - 97) % 26 + 97)
        possible_keys.append(decipher)
    
    else:
        for key in range(len(alphabet_upper)):
            decipher = " "
            for letter in text:
                if letter in alphabet_upper:
                    position = alphabet_upper.find(letter)
                    position -= key
                    if position < 0:
                        position = position + len(alphabet_upper)
                    decipher += alphabet_upper[position]

                elif letter in alphabet_lower:
                    position = alphabet_lower.find(letter)
                    position -= key
                    if position < 0:
                        position += len(alphabet_lower)
                    decipher += alphabet_lower[position]

                else:
                    decipher += letter
            possible_keys.append(decipher)

    return possible_keys
                    