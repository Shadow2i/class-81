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
        
def decipher(ciphertext, n):
    
    global capitalLetters, lowerLetters, numbers
    plaintext = ""

    for char in ciphertext:
        if char in numbers:
            currentPosition = numbers.find(char)
            plaintext += numbers[(currentPosition - n) % 10]
        elif char in lowerLetters:
            currentPosition = lowerLetters.find(char)
            plaintext += lowerLetters[(currentPosition - n )% 26] 
        elif char in capitalLetters:
            currentPosition = capitalLetters.find(char)
            plaintext += capitalLetters[(currentPosition - n) % 26] 
        else:
            plaintext += char
            
    return(plaintext)