import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

def nothing(x):
    pass

def plot_curve(f):
    fig = plt.figure(figsize=(15,5))
    gs = gridspec.GridSpec(2,3)
    x = np.arange(256)

    ax2 = fig.add_subplot(gs[:,1])
    ax2.set_title('Tone Curve')
    ticks = [0,42,84,127,169,211,255]
    ax2.set_xlabel('Input')
    ax2.set_ylabel('Output')
    ax2.set_xticks(ticks)
    ax2.set_yticks(ticks)
    y = 255 * (x / 255) ** (1/((f+0.01)/100))
    plt.plot(x,y)
    plt.draw()

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('gamma','image',1,100,nothing)

while(True):

    # Capture frame-by-frame
    ret, frame = cap.read()

    gamma = cv2.getTrackbarPos('gamma','image')
    imax = frame.max()
    y = imax * (frame / imax) ** (1/((gamma+0.01)/100))

    plot_curve(gamma)
    # Display the resulting frame
    cv2.imshow('image', y)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
plt.close()
