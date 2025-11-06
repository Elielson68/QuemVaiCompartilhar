import gevent.monkey
gevent.monkey.patch_all()

from flask import Flask, render_template
from flask_socketio import SocketIO
from share import ShareToday
import json
from data_controller import DataController
from api.quemvaiapi import bp as api_bp

app = Flask(__name__)
socketio = SocketIO(app)
app.socketio = socketio

data_controll = DataController()
data_controll.LoadData()
names = data_controll.GetNames()
print("nomes:", names)
share_today = ShareToday(names, data=data_controll.GetData())
app.share_today = share_today
app.register_blueprint(api_bp)

@app.route('/')
def home():
    worker = share_today.WhoShareToday()
    pending = share_today.PendingWorkers()
    print("EStá pausado? ", share_today.IsPaused())
    return render_template("home.html", worker=worker, pending=pending, paused=share_today.IsPaused())


@app.route('/reset')
def reset():
    share_today.Reset()
    share_today.SaveData()
    return "Index resetado!"


@app.route('/load')
def load():
    data_controll.LoadData()
    share_today.LoadData(data_controll.GetData())
    return "Dados carregados!"


@socketio.on('next')
def next_request():
    worker = share_today.WhoShareToday(jump=True)
    data = {'worker': worker, 'pending': share_today.PendingWorkers()}
    print("Recebeu a chamada de NEXT")
    socketio.emit("nextWorker", data)

@socketio.on('pause')
def pause_request():
    print("Pediu para pausar")
    share_today.RequestPause()
