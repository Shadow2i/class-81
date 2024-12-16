AllCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()}{\/?'

def cipher(plaintext, n):
    global  AllCharacters
    ciphertext = ''

    # Use 'getKey(n)' method to get the key and save it in 'n'
    

    for char in plaintext:
        if char in AllCharacters:
            currentPosition = AllCharacters.find(char)
            ciphertext += AllCharacters[(currentPosition + n ) % 77]
        else:
            ciphertext += char

    return ciphertext
        
def decipher(ciphertext, n):
    global  AllCharacters
    plaintext = ""

    # Use 'getKey(n)' method to get the key and save it in 'n'
    

    for char in ciphertext:
        if char in AllCharacters:
            currentPosition = AllCharacters.find(char)
            plaintext += AllCharacters[(currentPosition - n) % 77]       
        else:
            plaintext += char
            
    return(plaintext)

# define getKey(n) function    

    # Set the key variable to 0
    
    # Check if 'n' is a string using isinstance(n, str) 
    
        # Loop through each 'char' in 'n' 
        
           # find ASCII code of "char" using 'ord(char)' and add it to key
           
    # Else make key equals to n      
    

    # Return the 'key'
    
