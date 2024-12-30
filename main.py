from src.preprocess import preprocess_image
from src.edges import detect_edges
from src.contours import find_contours, save_contours
from src.visualize import save_and_show_result

def main():
    # Paths
    img_path = "image.png"
    output_dir = "output"
    result_path = f"{output_dir}/result.jpg"

    # Step 1: Preprocess the image
    img, binary = preprocess_image(img_path)

    # Step 2: Detect edges
    edges = detect_edges(binary)

    # Step 3: Find contours
    contours = find_contours(edges)

    # Step 4: Draw contours and save points
    output_img = save_contours(img, contours, output_dir)

    # Step 5: Save and show the result
    save_and_show_result(output_img, result_path)

if __name__ == "__main__":
    main()
