from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

    <DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-sarif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
    
        <body>
            <form action="/form" method="POST">
                <label>Rotate by:
                <input name="rot" type="text" id="text" value="0"/>
                </label>
                <input type="Submit"/>
                <textarea name="textbox"></textarea>
            </form>
        </body>
    </html>
    """

@app.route("/form", methods = ['POST'])
def encrypt():
    rotate_amt = request.form['rot']
    rot_amt_int = int(rotate_amt)
    text_entered = request.form['textbox']
    cyphered = rotate_string(text_entered, rot_amt_int)
    return "<h1>" + cyphered + "<h1>"

@app.route("/")
def index():
    return form
    

app.run()