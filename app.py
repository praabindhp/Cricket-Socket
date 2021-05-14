from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

@app.route("/", methods = ['GET', 'POST'])
def index():
    messages = ['Message One', 'Message Two', 'Message Three']
    return render_template("index.html", messages = messages)

@socketio.on('message')
def handleMessage(msg):
    print('Message : ' + msg)
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app)