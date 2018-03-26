from flask import *
from twilio.rest import Client
app= Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/send', methods= ['POST'])
def send():
    number=request.form['inputNumber']
    text=request.form['inputMessage']
    account=request.form['inputSID']
    token=request.form['inputTOKEN']
    twilio_number=request.form['inputTWILIONUMBER']
    client = Client(account, token)
    response = client.messages.create(to=number, from_=twilio_number, body=text)
    return '''<h1>Thanks john we will notify you every hour except the hours when are in deep sleep</h1>'''
if __name__=='__main__':
    app.run(debug=True)

































    










