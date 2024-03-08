import cv2

# Initialize the background Subtractor
bg_sub = cv2.createBackgroundSubtractorMOG2(detectShadows=True, varThreshold=100, history=2000)

# Set up a kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

def is_person_present(frame, threshold=1100):
    global bg_sub

    # Apply background subtraction
    fg_mask = bg_sub.apply(frame)

    # Get rid of shadows
    _, fg_mask = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)

    # Apply some morphological operations to ensure a good mask
    fg_mask = cv2.dilate(fg_mask, kernel, iterations=4)

    # Detect contours in the frame
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if there is a contour and the area is higher than the threshold
    if contours and cv2.contourArea(max(contours, key=cv2.contourArea)) > threshold:
        # Get the max contour
        cnt = max(contours, key=cv2.contourArea)

        # Draw a bounding box around the person and label it as person detected
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, 'Person Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)

        return True, frame

    # Otherwise, report that no one is present
    else:
        return False, frame
