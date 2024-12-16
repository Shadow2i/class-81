Create deCipher function
=======================

In this activity, you will learn to create the decipher function to decipher the deCiphered data and get the original values.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/40bc226a-13c1-4117-9d01-2abfd104ffaf.gif" width = "480" height = "320">


Follow the given steps to complete this activity:
1. Create deCipher function

* Open file `encryption.py`

* Declare a function called `deCipher()` which takes 2 parameters `ciphertext` and `n`.
  Plaintext will be the text to be ciphered and n will be the key.

  `def deCipher(ciphertext, n):`

* Declare global variables `capitalLetters, lowerLetters, numbers`.

    `global  capitalLetters, lowerLetters, numbers`

* Declare a variable `plaintext` and set and empty string to it.
    
    `plaintext = ''`

* Loop through the `plaintext` using for loop.

    `for char in plaintext:`

* Check if the `char` belongs to the `numbers`.

    `if char in numbers:`

* Find the current position of the `char` in the numbers using `numbers.find(char)` and store the value to the `currentPosition` variable.

    `currentPosition = numbers.find(char)`
    
* Get the current number after the shift by `n` and mod it by `10` so that it doesn't exceed the 10 numbers and add it to the `plaintext`.

    `plaintext += numbers[(currentPosition - n ) % 10]`

* Add another condition to check if the `char` belongs to the lower letters.
* Get the current position of the `char` from the  `lowerLetters`.
* Get the updated position of the `char` and add it to the `plaintext`, mod it by 26 so that the position remains in the 26 letters only.

    `elif char in lowerLetters:`

        `currentPosition = lowerLetters.find(char)`
        
        `plaintext += lowerLetters[(currentPosition - n )% 26]`

* Add another condition to check if the `char` belongs to the capital letters.
* Get the current position of the `char` from the  `capitalLetters`.
* Get the updated position of the `char` and add it to the `plaintext`, mod it by 26 so that   the position remains in the 26 letters only.

    `elif char in capitalLetters:`
    
        `currentPosition = capitalLetters.find(char)`
        
        `plaintext += capitalLetters[(currentPosition - n) % 26]`

* Add and else condition to add the `char` to the `plaintext` if other conditions are not met.

    `else:`

        `plaintext += char`

* Return the `plaintext`.

    `return plaintext`

2.  Call the function 

* Open file main.py.

* Call the `cipher` function for sender,receiver and amount` and pass their specific data and 2 as the key to the functions. 

    `sender = deCipher(sender, 2)`

   `receiver = deCipher(receiver, 2)`

    `amount = deCipher(amount, 2)`
`

* Create the object `deCipherData` and set the `sender, receiver and amount` as key and value pairs.

  `deCipherData = {`
   
    `"sender": sender,`

    `"receiver": receiver,`

    `"amount": amount`

    `}`
        
*  Print the `deCipherData`.

    `print(deCipherData)`

* Save and run the code to check the output.

