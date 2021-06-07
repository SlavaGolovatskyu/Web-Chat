from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socket = SocketIO(app)

COUNT_ONLINE_USERS = 0


@app.route('/', methods=['POST', 'GET'])
def test():
    return render_template('socket.html', online=COUNT_ONLINE_USERS)


@socket.on('connect_user')
def connect_user(data):
    global COUNT_ONLINE_USERS
    COUNT_ONLINE_USERS += 1
    print(data)
    emit('get_online', COUNT_ONLINE_USERS, broadcast=True)


@socket.on('disconnect')
def test_disconnect():
    global COUNT_ONLINE_USERS
    COUNT_ONLINE_USERS -= 1
    emit('get_online', COUNT_ONLINE_USERS, broadcast=True)


@socket.on('send_message')
def send_message(msg: dict):
    emit('take_msg', msg['msg'], broadcast=True)


if __name__ == '__main__':
    socket.run(app, debug=True)

