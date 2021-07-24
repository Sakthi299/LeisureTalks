from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mattram#ondre#marathathu'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event') # event handlers using socketio.on decorator 
def handle_my_custom_event(json, methods=['GET', 'POST']): # this view receives json object
    print('received my event: ' + str(json))  # prints on terminal
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)


# https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
