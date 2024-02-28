from flask import Flask, render_template
from flask_socketio import SocketIO
from share import ShareToday
import json
from data_controller import DataController

app = Flask(__name__)
socketio = SocketIO(app)


order_apresentation = ["Lamin", "Geison", "Ruilan", "Kelvin", "Tenis", "Jhone", "Iury", "Feitosa",
                          "Campos", "Domingues", "Fagundes", "Elielson"]
data_controll = DataController()
data_controll.LoadData()
share_today = ShareToday(order_apresentation, data=data_controll.GetData())


@app.route('/')
def home():
    worker = share_today.WhoShareToday()
    pending = share_today.PendingWorkers()
    print("EStá pausado? ", share_today.IsPaused())
    return render_template("home.html", worker=worker, pending=pending, paused=share_today.IsPaused())


@app.route('/reset')
def reset():
    share_today.Reset()
    return "Index resetado!"


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