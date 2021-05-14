from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
socketio = SocketIO(app)

history = []

@socketio.on('message')
def handleMessage(msg):
    history.append(msg)
    print('Message : ' + msg)
    print(history)
    send(msg, broadcast=True)
    return render_template("index.html", history = history)

@app.route("/")
def start():
    print(history)
    return render_template("index.html")

@app.route("/chat")
def chat():
    print(history)
    return render_template("chatPage.html")

if __name__ == '__main__':
	socketio.run(app)