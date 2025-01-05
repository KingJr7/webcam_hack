import socketio
import cv2
import base64
import numpy as np

sio = socketio.Client()

@sio.event
def connect():
    print("Connecté au serveur !")

@sio.on('frame_response')
def handle_frame_response(data):
    decoded_data = base64.b64decode(data)
    np_data = np.frombuffer(decoded_data, dtype=np.uint8)
    frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    if frame is not None:
        cv2.imshow("capture de la webcam (reçue)", frame)
        if cv2.waitKey(1) == 27:  # Échap pour fermer
            cv2.destroyAllWindows()
            sio.disconnect()


sio.connect('http://localhost:5000', transports=['websocket'])
sio.wait()
# capture_and_send()
