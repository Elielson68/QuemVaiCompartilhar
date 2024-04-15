from flask import Blueprint, current_app, jsonify

bp = Blueprint("api", __name__, url_prefix='/api/v1')

@bp.route("/jump", methods=["POST"])
def jump():
    worker = current_app.share_today.WhoShareToday(jump=True)
    data = {'worker': worker, 'pending': current_app.share_today.PendingWorkers()}
    print("API - Recebeu a chamada de NEXT")
    current_app.socketio.emit("nextWorker", data)
    return jsonify({"status": "jumped"})


@bp.route("/pause", methods=["POST"])
def pause():
    print("API - Pediu para pausar")
    current_app.share_today.RequestPause()
    return jsonify({"status": "paused"})
