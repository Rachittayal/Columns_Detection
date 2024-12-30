import cv2

def detect_edges(binary_img):
    edges = cv2.Canny(binary_img, 1, 500)
    return edges
