#caesar cipher
def encrypt_text(plaintext, n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)
    
    return ans

def decrypt_text(ciphertext, n):
    ans = ""
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) - n - 97) % 26 + 97)
    
    return ans

inp = int(input("Choose \n 1.Encryption\n 2. Decryption\n"))
if inp == 1:
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = encrypt_text(plaintext, shift)
    print("Encrypted Text is: " + encrypted_text)
elif inp == 2:
    encrypted_text = input("Enter the encrypted text: ")
    shift = int(input("Enter the shift value: "))
    plaintext = decrypt_text(encrypted_text, shift)
    print("Decrypted Text is: " + plaintext)
else:
    print("Invalid Choice!(1/2)")
