Use string to cipher the text
==============================

In this activity, you will learn to use the string to cipher the text.


<img src= "https://media.slid.es/uploads/1525749/images/10631817/AA2.gif" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Create the getKey function.

* Open file `cipher.py`

* Define function named `getKey(n)`.

    `def getKey(n):`
    
* Set the `key` variable to `0`.

    `key = 0`

* Check if `n` is a string using `isinstance(n, str)`.

    `if isinstance(n,str):`

* Loop through each `char` in `n`.

    `for char in n:`

* Find ASCII code of `char` using `ord(char)` and add it to key.

    `key += ord(char)`

* Else set `n` to the `key` variable.

    `else:`

        `key = n`

* Return the `key`.

    `return key`

2. Use the function

* Use `getKey(n)` method to get the key and save it in `n` in the cipher function.

    `n =getKey(n)`

* Use the same in the decipher function. 

* Save and run the code to check the output.

