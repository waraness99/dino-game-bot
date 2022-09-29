
import cv2
import numpy as np
import pyautogui
import time
import mss
import mss.tools

PIXEL_COLOR_LIMIT = 100
PIXEL_LIMIT_MAX = 30000
PIXEL_LIMIT_MIN = 3500


def main():
    # wait 5 seconds before starting
    time.sleep(5)
    while True:
        # take screenshot
        with mss.mss() as sct:
            region = {'top': 226, 'left': 650, 'width': 72, 'height': 72}
            image = sct.grab(region)
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # count pixels
        black_pixel_count = np.sum(image < PIXEL_COLOR_LIMIT)
        white_pixel_count = np.sum(image > PIXEL_COLOR_LIMIT)

        # light mode
        if black_pixel_count > PIXEL_LIMIT_MIN and black_pixel_count < PIXEL_LIMIT_MAX:
            jump()
        # dark mode
        if white_pixel_count > PIXEL_LIMIT_MIN and white_pixel_count < PIXEL_LIMIT_MAX:
            jump()

        # display image
        cv2.imshow('image', image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def jump():
    pyautogui.keyDown('space')
    time.sleep(0.001)
    pyautogui.keyUp('space')


if __name__ == "__main__":
    main()
