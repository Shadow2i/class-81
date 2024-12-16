Cipher the Special Characters
==============================

In this activity, you will learn to optimize the code and cipher the special characters.


<img src= "https://media.slid.es/uploads/1525749/images/10631842/AA1.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Optimize the code.

* Open file `cipher.py`

* Create a string of all the availabe characters. Also include the special characters.

    `AllCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()}{\/?'`

* Access `AllCharacters` as global.

    `global  AllCharacters`

*  Check if `char` exits in `AllCharacters`.

    `if char in AllCharacters:`

* Find position of `char` in `AllCharacters`.

    `currentPosition = AllCharacters.find(char)`

* Get the current position of the character and shift it up with the key and add it to the cipherText.

    `ciphertext += AllCharacters[(currentPosition + n ) % 77]`

* Remove the rest of elif conditions.

* Save and run the code to check the output.

