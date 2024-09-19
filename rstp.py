import cv2

rtsp_url = 'your rtsp url here'

cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print(f"Erro ao conectar ao stream: {rtsp_url}")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Falha ao receber frame, saindo...")
        break

    cv2.imshow('RTSP Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
