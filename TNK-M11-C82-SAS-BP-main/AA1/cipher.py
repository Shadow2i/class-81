capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
# Create a list AllCharacters


def cipher(plaintext, n):
    # Access AllCharacters as global
    global  capitalLetters, lowerLetters, numbers
    ciphertext = ''

    for char in plaintext:
        # Check if char exits in AllCharacters
        if char in numbers:
            # Find position of char in AllCharacters
            currentPosition = numbers.find(char)
            # Calculate the cipher text as AllCharacters[(currentPosition + n ) % 77]
            ciphertext += numbers[(currentPosition + n ) % 10]
        # Remove rest of the elif's
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            ciphertext += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            ciphertext += capitalLetters[(currentPosition + n) % 26]
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    # Access AllCharacters as global
    global capitalLetters, lowerLetters, numbers
    plaintext = ""

    for char in ciphertext:
         # Check if char exits in AllCharacters
        if char in numbers:
            # Find position of char in AllCharacters
            currentPosition = numbers.find(char)
            # Calculate the cipher text as AllCharacters[(currentPosition - n ) % 77]
            plaintext += numbers[(currentPosition - n) % 10]
        # Remove rest of the elif's
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            plaintext += capitalLetters[(currentPosition - n) % 26] 
        else:
            plaintext += char
            
    return(plaintext)
