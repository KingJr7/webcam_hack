from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialisation de l'application Flask et du serveur SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")  # Autorise toutes les origines pour les tests locaux

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Gestion des messages WebSocket
@socketio.on('message')
def handle_message(msg):
    print(f"Message reçu")
    # Réponse au client
    send(f"Serveur a reçu : {msg}", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
