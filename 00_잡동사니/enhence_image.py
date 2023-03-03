# Import necessary libraries
import cv2
import numpy as np

# Load the raw data from the thermal camera
# Load the raw data as a grayscale image
raw_data = cv2.imread("grayscale_image.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is empty
if raw_data is None:
    print("Error: Could not load image data from file")
else:
    # Apply image processing techniques to improve the image quality
    # Apply a median blur to reduce noise
    filtered_data = cv2.medianBlur(raw_data, 5)
    # Sharpen the image using an unsharp masking filter
    sharpened_data = cv2.addWeighted(raw_data, 1.5, filtered_data, -0.5, 0)
    # Enhance the contrast using histogram equalization
    enhanced_data = cv2.equalizeHist(sharpened_data)

    # Display the raw and processed data
    cv2.imshow("Raw data", raw_data)
    cv2.imshow("Processed data", enhanced_data)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
