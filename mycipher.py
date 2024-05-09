# CSCI213CeasarCipherProject
def cipher(user_text, n):
    ans = ""
    for i in range(len(user_text)):
        ch = user_text[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)
    return ans

user_text = input("Enter text to encrypt: ")
n = int(input("Enter the shift pattern (integer): "))
print("Plain Text is: " + user_text)
print("Shift pattern is: " + str(n))
print("Cipher Text is: " + cipher(user_text, n))
