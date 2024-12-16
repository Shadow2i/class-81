capitalLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'

def cipher(plaintext, n):
    global  capitalLetters, lowerLetters, numbers
    ciphertext = ''

    for char in plaintext:
        if char in numbers:
            currentPosition = numbers.find(char)
            ciphertext += numbers[(currentPosition + n ) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            ciphertext += lowerLetters[(currentPosition + n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            ciphertext += capitalLetters[(currentPosition + n) % 26] 
        else:
            ciphertext += char

    return ciphertext
        
# Define the function decipher() that takes two parameter i.e 'ciphertext' and a key 'n'
def deCipher(ciphertext, n):
    # Access globals: capitalLetters, lowerLetters, numbers
    global  capitalLetters, lowerLetters, numbers
    # Create empty string variable plaintext
    plaintext = ''

    # Loop throught each 'char' in the 'ciphertext'
    for char in plaintext:
        # Check if 'char' is present in 'numnbers' list
        if char in numbers:
            # Get the current position of the 'char' in 'numbers' list
            currentPosition = numbers.find(char)
            # Calculate the character using formula : numbers[(currentPosition - n) % 10] and add it to plaintext
            plaintext += numbers[(currentPosition - n ) % 10]
        # Check if 'char' is present in 'lowerLetters' list
        elif char in lowerLetters:
            # Get the current position of the 'char' in 'lowerLetters' list
            currentPosition = lowerLetters.find(char)
            # Calculate the character using formula : lowerLetters[(currentPosition - n )% 26] and add it to plaintext
            plaintext += lowerLetters[(currentPosition - n )% 26]
        # Check if 'char' is present in 'capitalLetters' list
        elif char in capitalLetters:
            # Get the current position of the 'char' in 'capitalLetters' list
            currentPosition = capitalLetters.find(char)
            # Calculate the character using formula : capitalLetters[(currentPosition - n) % 26] and add it to plaintext
            plaintext += capitalLetters[(currentPosition - n) % 26]
            
        # Else add the 'char' to 'plaintext'
        else:
            plaintext += char

    # Return 'plaintext'
    return plaintext