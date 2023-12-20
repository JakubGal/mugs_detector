# Circle Detection in Video using OpenCV

This Python script utilizes OpenCV to detect circular shapes (like mugs) in a video file. It reads frames from a video, converts them to grayscale, applies a blur for noise reduction, and then uses the Hough Circle Transform method to detect circles.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.x
- OpenCV library for Python

You can install OpenCV using pip:

```bash
pip install opencv-python
```

## Usage

Video:
https://drive.google.com/drive/folders/1ajL1xhN_OhVXXcpvuZrW5EYdA_5qX9Xc?usp=sharing

https://www.youtube.com/watch?v=-sG3lcZDDDs

Place the video file you want to analyze in the same directory as the script, or provide the path to the video file in the script.
Run the script:

```bash

python circle_detection.py
```
  The script will open a window showing the video with detected circles highlighted. Each circle will be marked with its circumference and center.
  The number of detected circles will be displayed on the top left of the video frame.
  To exit the video, press 'q'.

## The circle detection parameters are set as follows:

    method: Detection method (using cv2.HOUGH_GRADIENT).
    dp: Inverse accumulator resolution ratio.
    minDist: Minimum distance between circle centers.
    param1: Higher threshold for the Canny edge detector.
    param2: Accumulator threshold for circle centers.
    minRadius: Minimum circle radius.
    maxRadius: Maximum circle radius.
