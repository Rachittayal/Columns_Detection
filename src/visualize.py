import cv2
import os

def save_and_show_result(img, output_path):
    cv2.imshow("Pillars", img)
    cv2.imwrite(output_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
