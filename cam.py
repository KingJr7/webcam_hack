import cv2
import socketio
import base64

sio = socketio.Client()
@sio.event
def connect():
    print("Connecté au serveur !")

@sio.event
def message(data):
    # print(f"Message reçu : {data}")
    pass

sio.connect('http://localhost:5000', transports=['websocket'])  # Connexion au serveur Flask

capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    
    _, buffer = cv2.imencode('.jpg', frame)  # Encodage de l'image en mémoire
    jpg_as_text = base64.b64encode(buffer).decode('utf-8')  # Encodage base64
    
    cv2.imshow("capture de la webcam", frame)
    sio.send(jpg_as_text)  # Envoi d'un message
    
    if cv2.waitKey(1) == 27:
        break
    
capture.release()
sio.wait()  # Garde la connexion ouverte
cv2.destroyAllWindows()

