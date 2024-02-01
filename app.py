from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
from share import ShareToday

fl = Flask(__name__)
app = SocketIO(fl)

share_today = ShareToday(["Elielson", "Lamin", "Feitosa", "Geison", "Kelvin", "Tenis", "Iury"])

@fl.route('/')
def home():
  worker = share_today.WhoShareToday()
  pending = share_today.PendingWorkers()
  return render_template("home.html", worker=worker, pending=pending)

@app.on('next')
def next_request():
    worker=share_today.WhoShareToday(jump=True)
    data = {'worker': worker, 'pending': share_today.PendingWorkers()}
    app.emit("nextWorker", data)

