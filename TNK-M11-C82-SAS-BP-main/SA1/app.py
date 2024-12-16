from flask import Flask, render_template, request
import os
# Import cipher from cipher.py


STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True


@app.route("/", methods= ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }
        
        # Cipher the sender, receiver and amount 
        sender = cipher(sender, 2)
        receiver = cipher(receiver, 2)
        amount = cipher(amount, 2)

        # Create a dictionary cipherData with sender, receiver and amount
        cipherData = {
        "sender": sender,
        "receiver": receiver,
        "amount": amount
        }
        # Print cipherData
        print(cipherData)
        
        return render_template('index.html', blockData = blockData)

if __name__ == '__main__':
    app.run(debug = True, port=4000)