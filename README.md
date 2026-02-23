# Disease-Detection-system
Chest X-ray Disease Detection using GLCM

📌 Overview

This project detects possible chest diseases (like pneumonia) from X-ray images using image processing and texture analysis techniques. It uses GLCM (Gray Level Co-occurrence Matrix) features to classify whether the chest X-ray is normal or abnormal.

⚠️ Disclaimer: This is a basic rule-based system for learning purposes and not a medical diagnostic tool.

🚀 Features

📷 X-ray image analysis

🧠 Texture-based feature extraction (GLCM)

🔍 Detects patterns like pneumonia

📊 Extracts key features:

Contrast

Energy

Homogeneity

🩺 Classifies:

Normal chest

Pneumonia detected

Abnormal (needs checkup)

🛠️ Technologies Used

Python

OpenCV (cv2)

NumPy

Matplotlib

scikit-image (skimage)

⚙️ How It Works
1. Image Loading

Reads X-ray image from local folder

Stops execution if image not found

2. Preprocessing

Convert to grayscale

Apply Gaussian blur (reduces noise)

Apply histogram equalization (improves contrast)

3. Feature Extraction (GLCM)

GLCM analyzes texture patterns in the image.

Extracted features:

Contrast → Difference between pixel intensities

Energy → Uniformity of texture

Homogeneity → Smoothness of image

4. Classification (Rule-Based)

High contrast + low energy → Pneumonia detected

High homogeneity → Normal chest

Otherwise → Abnormal (needs checkup)

📂 Project Structure
chest-xray-detection/
│── xray_analysis.py
│── R.jpeg
│── README.md
▶️ How to Run
Step 1: Install Dependencies
pip install opencv-python numpy matplotlib scikit-image
Step 2: Add Image

Place your X-ray image (e.g., R.jpeg) in the project folder

Step 3: Run the Program
python xray_analysis.py
📊 Sample Output
========= EXTRACTED FEATURES =========
Contrast     : 25.3421
Energy       : 0.0821
Homogeneity  : 0.5123

========= DIAGNOSIS RESULT =========
Detected Condition: PNEUMONIA DETECTED
====================================
⚠️ Limitations

Not medically accurate

Uses simple rule-based logic

No trained machine learning model

Sensitive to image quality

💡 Future Improvements

🤖 Train CNN model for better accuracy

📊 Use large medical datasets

🌐 Build web app for predictions

📱 Mobile health application

🧠 Integrate deep learning (TensorFlow/PyTorch)

👩‍💻 Author

Priyanka S

Information Science Engineering Student

Interested in AI, Image Processing & Cybersecurity
