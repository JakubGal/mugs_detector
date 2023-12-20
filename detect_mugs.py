import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('mugs_video.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
        # Convert to grayscale. 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    
    '''
    method: Detection method, either HOUGH_GRADIENT or HOUGH_GRADIENT_ALT.

    dp: Inverse accumulator resolution ratio. dp=1: same as image resolution; 
    dp=2: half resolution. For HOUGH_GRADIENT_ALT, dp=1.5 is recommended.

    minDist: Minimum distance between circle centers to avoid false detections.

    param1: For HOUGH_GRADIENT and HOUGH_GRADIENT_ALT, 
    it's the higher Canny edge detector threshold. HOUGH_GRADIENT_ALT typically needs a higher value.

    param2: For HOUGH_GRADIENT, it's the accumulator threshold for circle centers. 
    For HOUGH_GRADIENT_ALT, it measures circle "perfectness" (0.9 is typical).

    minRadius: Minimum circle radius.

    maxRadius: Maximum circle radius. If ≤ 0, uses maximum image dimension
    
    '''
    
    method = cv2.HOUGH_GRADIENT
    dp = 1
    minD = 90
    p1 = 100
    p2 = 60
    minR = 50
    maxR = 120

    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,  
    method, dp, minD, param1 = p1, param2 = p2, minRadius=minR, maxRadius=maxR) 
    
    # Draw circles that are detected.
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        cups = 0
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
    
            # Draw the circumference of the circle. 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
    
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            cups += 1
        frame = cv2.putText(frame, str(cups), (50, 50), cv2.FONT_HERSHEY_SIMPLEX ,  
                   2, (255,0,0), 2, cv2.LINE_AA) 
   
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
print('Detection finished')
# Closes all the frames
cap.release()
cv2.destroyAllWindows()

