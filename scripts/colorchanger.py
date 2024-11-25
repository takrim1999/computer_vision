import cv2 as cv
import numpy as np


# Your 3D array
# Calculate the sum of each subarray

def replace_subarrays(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(sum(array[i][j]))
            # if sum(array[i][j]) < 20:
            #     array[i][j] = [255, 255, 255]

capture = cv.VideoCapture(0)
# print(capture.read()[1])
while True:
    Frame = capture.read()[1]
    original_array = np.array(Frame)
    subarray_sums = np.sum(original_array, axis=-1)
    mask = (subarray_sums > 100) & (subarray_sums < 180)
    original_array[mask] = [34, 88, 226]
    cv.imshow("Video",original_array)
    # cv.imshow("Video",replace_subarrays(original_array))
    if cv.waitKey(20) and (0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()