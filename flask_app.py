from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

COUNT_ONLINE_USERS = 1


@app.route('/', methods=['POST', 'GET'])
def test():
    return render_template('socket.html', online=COUNT_ONLINE_USERS)


@socketio.on('connect_user')
def connect_user(data):
    global COUNT_ONLINE_USERS
    COUNT_ONLINE_USERS += 1
    print(data['data'])
    print('users online: ', COUNT_ONLINE_USERS)


@socketio.on('disconnect')
def test_disconnect():
    global COUNT_ONLINE_USERS
    COUNT_ONLINE_USERS -= 1
    print('Client disconnected')
    print('users online: ', COUNT_ONLINE_USERS)


@socketio.on('send_message')
def send_message(msg):
    emit('take_msg', (msg['msg'], COUNT_ONLINE_USERS), broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)

