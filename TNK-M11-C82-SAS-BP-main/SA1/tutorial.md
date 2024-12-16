Create Cipher function
=======================

In this activity, you will learn to create the cipher the data for the text entered in lower case or upper case user.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/5b0ac495-8412-49a2-9245-8d37e1927a37.gif" width = "480" height = "320">


Follow the given steps to complete this activity:
1. Create Cipher function

* Open file `cipher.py`.

* Add a condition to check if the `char` belongs to the lower letters.
* Get the current position of the `char` from the  `lowerLetters`.
* Get the updated position of the `char` and add it to the `cipherText`, mod it by 26 so that the position remains in the 26 letters only.

    `elif char in lowerLetters:`

        `currentPosition = lowerLetters.find(char)`
        
        `cipherText += lowerLetters[(currentPosition + n )% 26]`

* Add another condition to check if the `char` belongs to the capital letters.
* Get the current position of the `char` from the  `capitalLetters`.
* Get the updated position of the `char` and add it to the `cipherText`, mod it by 26 so that   the position remains in the 26 letters only.

    `elif char in capitalLetters:`
    
        currentPosition = capitalLetters.find(char)
        
        cipherText += capitalLetters[(currentPosition + n) % 26]


2.  Call the function 

* Open file main.py.

* Call the `cipher` function for sender,receiver and amount` and pass their specific data and 2 as the key to the functions. 

    `sender = cipher(sender, 2)`

   `receiver = cipher(receiver, 2)`
   
    `amount = cipher(amount, 2)`
`

* Create the object `cipherData` and set the `sender, receiver and amount` as key and value pairs.

  `cipherData = {`
   
    `"sender": sender,`

    `"receiver": receiver,`

    `"amount": amount`

    `}`
        
*  Print the `cipherData`.

    `print(cipherData)`

* Save and run the code to check the output.

