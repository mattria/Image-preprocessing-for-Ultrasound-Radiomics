Image Preprocessing for Ultrasound Radiomics

This repository contains Python scripts designed to preprocess ultrasound images for radiomics analysis. The preprocessing methods implemented include:
-Histogram Equalization
-Standard CLAHE (Contrast Limited Adaptive Histogram Equalization)
-Advanced CLAHE (with adjustable clip limit and adaptive tile grid size)

Folder Structure
The repository is organized into three main directories, each corresponding to a different preprocessing technique:
Image-preprocessing-for-Ultrasound-Radiomics/
─ histogram_equalization/histogram_equalization.py
─ standard_clahe/standard_clahe.py
─ advanced_clahe/advanced_clahe.py

Preprocessing Methods

1. Histogram Equalization:
Histogram Equalization is a global technique that enhances image contrast by distributing the most frequent intensity values across the entire grayscale spectrum. This method can significantly improve the overall visibility of features within an image. However, it may also introduce artifacts or fail to effectively address local contrast issues, which can result in the loss of detail in certain areas of the image.

2. Standard CLAHE (Contrast Limited Adaptive Histogram Equalization):
Standard CLAHE is a localized contrast enhancement technique that divides the image into small regions, known as tiles, and applies histogram equalization to each one independently. In this implementation, the method uses a clip limit of 2.0 and a fixed tile grid size of 8 by 8 pixels. While this approach can lead to more pronounced contrast improvements across different regions of the image, the higher clip limit may increase the likelihood of introducing noise, particularly in areas of uniform intensity.

3. Advanced CLAHE (Contrast Limited Adaptive Histogram Equalization):
The Advanced CLAHE method builds on the standard approach by offering a more adaptive contrast enhancement. It uses a lower clip limit of 0.9 and a dynamically calculated tile grid size set to approximately 64 pixels. This technique aims to provide subtler, image-specific improvements, reducing the risk of noise and artifacts while maintaining effective contrast enhancement. The adaptability of the tile grid size allows the method to better handle variations in image size and content, resulting in a more balanced enhancement.

Usage
Each script can be run to preprocess ultrasound images by following these steps:
Prepare your input images: Place your ultrasound images in a directory such as input_images/.
Run the script: Execute the corresponding Python script to apply the preprocessing method.
Save the output: The processed images will be saved to the specified output directory.

Requirements
The scripts require the following Python libraries:
OpenCV (cv2) for image processing.
OS (os) for handling file and directory operations.
You can install OpenCV using pip
