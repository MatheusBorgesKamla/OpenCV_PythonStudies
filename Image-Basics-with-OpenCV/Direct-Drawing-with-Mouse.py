import cv2
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Create a function based on a CV2 Event (Left button click)
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),-1)

def drawing_circles():
    
    # This names the window so we can reference it 
    cv2.namedWindow('My_Drawing',cv2.WINDOW_NORMAL)
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('My_Drawing',draw_circle)

    while True: #Runs forever until we break with Esc key on keyboard
        # Shows the image window
        cv2.imshow('My_Drawing',img)
        # EXPLANATION FOR THIS LINE OF CODE:
        if cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()
    return

drawing_circles()

# Create a function based on a CV2 Event (Left button click)
drawing = False # True if mouse is pressed
#Inicial coordinates
ix,iy = -1,-1

# Create a black image
img1 = np.zeros((512,512,3), np.uint8)

def drawing_rectangles():
    cv2.namedWindow('My_Rectangle',cv2.WINDOW_NORMAL)
    # Connects the mouse button to our callback function
    cv2.setMouseCallback('My_Rectangle',draw_rectangle)

    while True: #Runs forever until we break with Esc key on keyboard
        # Shows the image window
        cv2.imshow('My_Rectangle',img1)
    
        # CHECK TO SEE IF ESC WAS PRESSED ON KEYBOARD
        if cv2.waitKey(1) == 27:
            break
        # Once script is done, its usually good practice to call this line
        # It closes all windows (just in case you have multiple windows called)
    cv2.destroyAllWindows()
    return

# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        # Now the mouse is moving
        if drawing == True:
            # If drawing is True, it means you've already clicked on the left mouse button
            # We draw a rectangle from the previous position to the x,y where the mouse is
            cv2.rectangle(img1,(ix,iy),(x,y),(0,255,0),-1)
           

    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv2.rectangle(img1,(ix,iy),(x,y),(0,255,0),-1)

drawing_rectangles()        