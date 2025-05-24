import sys
from importlib.metadata import version

import cv2 as cv


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def main():
    flags = [i for i in dir(cv) if i.startswith('COLOR_')]
    print(flags)
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    loop_count = 0
    while True:
        loop_count += 1
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # FAILS: gray = cv.cvtColor(frame, cv.COLOR_BAYER_BG2BGR)
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        #cv.imshow('frame', gray)
        cv.imshow('frame', frame)
        # break out of the loop when the user presses the "q" key
        if cv.waitKey(1) == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()
    print(f'loop count = {loop_count}')


if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    print(f'OpenCV version: {get_package_version("opencv-python")}')

    main()
