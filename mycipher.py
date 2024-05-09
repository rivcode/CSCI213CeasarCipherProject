# CSCI213CeasarCipherProject
import sys

# Check Python version
if sys.version_info.major < 3:
    # Python 2
    input_func = raw_input
else:
    # Python 3
    input_func = input

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

user_text = input_func("Enter text to encrypt: ")
n = int(input_func("Enter the shift pattern (integer): "))
print("Plain Text is: " + user_text)
print("Shift pattern is: " + str(n))
print("Cipher Text is: " + cipher(user_text, n))
