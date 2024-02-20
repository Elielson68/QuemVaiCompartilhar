from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from share import ShareToday

app = Flask(__name__)
socketio = SocketIO(app)

share_today = ShareToday(["Kelvin", "Tenis", "Jhone", "Iury", "Feitosa",
                          "Campos", "Domingues", "Fagundes", "Elielson", "Lamin", "Geison", "Ruilan"])

@app.route('/')
def home():
  worker = share_today.WhoShareToday()
  pending = share_today.PendingWorkers()
  return render_template("home.html", worker=worker, pending=pending)


@app.route('/reset')
def reset():
  share_today.Reset()
  return "Index resetado!"


@socketio.on('next')
def next_request():
    worker=share_today.WhoShareToday(jump=True)
    data = {'worker': worker, 'pending': share_today.PendingWorkers()}
    print("Recebeu a chamada de NEXT")
    socketio.emit("nextWorker", data)
