import cv2
import os
import numpy as np

def find_contours(edge_img):
    contours, _ = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def save_contours(img, contours, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img_copy = img.copy()

    for i, contour in enumerate(contours):
        color = np.random.randint(0, 255, size=3).tolist()  # Random color for each pillar
        cv2.drawContours(img_copy, [contour], -1, color, thickness=2, lineType=cv2.LINE_AA)

        # Save the contour points to a file
        points_file = os.path.join(output_dir, f"pillar_{i+1}.txt")
        with open(points_file, "w") as f:
            for point in contour:
                x, y = point[0]
                f.write(f"{x}, {y}\n")

    return img_copy