import cv2
import numpy as np
import os
from tqdm import tqdm

def main():   
    # Playing video from file
    # vid = cv2.VideoCapture(str(file_path))
    vid = cv2.VideoCapture('./videos/walkman_silhh.mp4')

    try:
        if not os.path.exists('data'):
            print("Creating '/data' directory..")
            os.makedirs('data')
        else:
            # already exists, clear
            print("'/data' directory found, clearing..")
            for file in os.listdir('data'):
                os.remove(os.path.join('data', file))
            print("'/data' cleared")
    except OSError:
        print('Error: Creating directory of data')

    interval = int(vid.get(cv2.CAP_PROP_FPS)) / 2
    totalFrames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    print("Total Frames: {}".format(totalFrames))

    while(vid.isOpened()):
        currentFrame = 0
        success, frame = vid.read()

        if success:
            while currentFrame < totalFrames/interval:
                # Capture frame-by-frame
                success, frame1 = vid.read()

                # Saves image of the current frame in jpg file
                name = './data/frame' + str(currentFrame) + '.png'
                print('Creating...' + name)
                cv2.imwrite(name, frame1)

                # To stop duplicate images
                currentFrame += 1
        vid.release()
        break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    main()