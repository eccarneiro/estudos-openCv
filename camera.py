import cv2
import datetime 
import platform 

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


if platform.system() == "Linux":
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
else:
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    print("Verifique se a câmera está conectada e não está sendo usada por outro aplicativo.")
    exit()

cv2.namedWindow('Camera com Detecção de Faces', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camera com Detecção de Faces', 960, 720)

face_count = 0 
total_faces_detected = 0 
last_detection_time = {}

print("Pressione 'q' para sair.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro: Falha ao ler o frame da câmera.")
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.15, 
        minNeighbors=6,  
        minSize=(60, 60)  
    )

    face_count = len(faces) 

    for i, (x, y, w, h) in enumerate(faces):
     
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'Face {i+1}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        is_new_face = True
        for face_id, last_time in last_detection_time.items():
            pass


    cv2.putText(frame, f'Faces no Frame: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, timestamp_str, (10, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow('Camera com Detecção de Faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()