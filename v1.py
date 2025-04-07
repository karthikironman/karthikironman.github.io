import cv2
import os

# Define Haar cascade path
haar_cascade_path = './haarcascade_frontalface_default.xml'

# Check if Haar cascade file exists
if not os.path.isfile(haar_cascade_path):
    print("Error: Haar cascade file not found.")
    exit()

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Load hat image
hat_img = cv2.imread('hat.png', cv2.IMREAD_UNCHANGED)

# Initialize video capture device
cap = cv2.VideoCapture(0)

while True:
    # Capture frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw hat on detected faces
    for (x, y, w, h) in faces:
        # Resize hat image to fit face
        resized_hat = cv2.resize(hat_img, (w, h // 2))

        # Calculate coordinates for hat placement
        hat_x = x
        hat_y = y - h // 2

        # Overlay hat on frame
        alpha_s = resized_hat[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s

        for c in range(0, 3):
            frame[hat_y:hat_y + resized_hat.shape[0], hat_x:hat_x + resized_hat.shape[1], c] = (
                alpha_s * resized_hat[:, :, c] +
                alpha_l * frame[hat_y:hat_y + resized_hat.shape[0], hat_x:hat_x + resized_hat.shape[1], c]
            )

    # Display filtered video capture
    cv2.namedWindow('Filtered Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Filtered Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Filtered Video', frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture device
cap.release()
cv2.destroyAllWindows()
