Display the Deciphered data
========================================

In this activity, you will learn to display the deciphered text on the html.


<img src= "https://media.slid.es/uploads/1525749/images/10632600/pasted-from-clipboard.png" width = "480" height = "320">


Follow the given steps to complete this activity:

1. Create div for deCiphered data.

* Open file `index.html`

* Add heading `Decipher Data` the `h4` tag.

    `<h4>Decipher Data:</h4>`

* Create the div with id `senderData` and access the `deCipherData["sender"]` key in it to display the sender data.

    `<div id="senderData">Sender: {{ deCipherData["sender"] }}</div>`

* Create the div with id `receiverData` and access the `cipherData["receiver"]` key in it to display the receiver data.

    `<div id="receiverData">Receiver: {{ deCipherData["receiver"] }}</div>`

* Create the div with id `amountData` and access the `deCipherData["amount"]` key in it to display the amount data.

	`<div id="amountData">Amount: {{deCipherData["amount"]}}</div>`

* Save and run the code to check the output.

