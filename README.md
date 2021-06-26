# Gaze Tracking

This is code contains dlib library that provides a **webcam-based eye tracking system**. Few changes were made to give you the exact position of the pupils and the gaze direction, in real time. For more information , refer gaze_tracking directory and documentation.


## Installation

Clone this project:

```
git clone 
```

Install the required dependencies :

```
pip install -r requirements.txt
```

Collect data:

```
python collect_data.py
```
Press "s" to start learning. Follow the mouse around and keep your eyes focused on it. By default the code runs for 5 mins . Increase the time and collect all possibile positions for better dataset.

Train model:

```
python train.py
```
Predict:

```
python predict.py
```
## Documentation

In the following examples, `gaze` refers to an instance of the `GazeTracking` class.

### Refresh the frame

```python
gaze.refresh(frame)
```

Pass the frame to analyze (numpy.ndarray). If you want to work with a video stream, you need to put this instruction in a loop, like the example above.

### Position of the left pupil

```python
gaze.pupil_left_coords()
```

Returns the coordinates (x,y) of the left pupil.

### Position of the right pupil

```python
gaze.pupil_right_coords()
```

Returns the coordinates (x,y) of the right pupil.

### Looking to the left

```python
gaze.is_left()
```

Returns `True` if the user is looking to the left.

### Looking to the right

```python
gaze.is_right()
```

Returns `True` if the user is looking to the right.

### Looking at the center

```python
gaze.is_center()
```

Returns `True` if the user is looking at the center.

### Left eye size

```python
ratio = gaze.get_left_eyesize()
```

Returns width and height of left eye bounding box.

### Right eye size

```python
ratio = gaze.get_right_eyesize()
```

Returns width and height of right eye bounding box.

### Horizontal direction of the gaze

```python
ratio = gaze.horizontal_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the horizontal direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0.

### Vertical direction of the gaze

```python
ratio = gaze.vertical_ratio()
```

Returns a number between 0.0 and 1.0 that indicates the vertical direction of the gaze. The extreme top is 0.0, the center is 0.5 and the extreme bottom is 1.0.

### Blinking

```python
gaze.is_blinking()
```

Returns `True` if the user's eyes are closed.

### Webcam frame

```python
frame = gaze.annotated_frame()
```

Returns the main frame with pupils highlighted.

