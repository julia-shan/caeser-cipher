from encrypt import encrypt
from decrypt import decrypt

def main(): 
    mode = input("Would you like to encrypt or decrypt? ")
    if (mode.lower() == "encrypt"):
        text = input("Enter text to encrypt: ")
        shift = input("Enter shift pattern number: ")
        if not type(shift) is int: 
            try: 
                shift = int(shift)
            except ValueError:
                print("Please enter an integer")
        print("Unencrypted text: " + text)
        print("Number of shifts: " + str(shift))
        print("Encrypted textt: " + encrypt(text, shift))
    if(mode.lower() == "decrypt"):
        text = input("Enter text to encrypt: ")
        shift = input("Enter shift pattern number if known else put 0: ")
        if not type(shift) is int: 
            try: 
                shift = int(shift)
            except ValueError:
                print("Please enter an integer")
        print("Encrypted text: " + text)
        print("Number of shifts: " + str(shift))
        print("Decrypted textt: " + encrypt(text, shift))

if __name__ == '__main__':
    main()