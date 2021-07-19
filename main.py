from encrypt import encrypt

def main(): 
    text = input("Enter text to encrypt: ")
    shift = input("Enter shift pattern number: ")
    if not type(shift) is int: 
        try: 
            shift = int(shift)
        except ValueError:
            print("Please enter an integer")
    print("Unencrypted Text: " + text)
    print("Number of shifts: " + str(shift))
    print("Cipher: " + encrypt(text, shift))

if __name__ == '__main__':
    main()