import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import graycomatrix, graycoprops

img_path = "R.jpeg"   # Put image in same folder
image = cv2.imread(img_path)

if image is None:
    print("ERROR: Image not found. Check image path.")
    exit()

# -----------------------------
# PREPROCESSING
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
equalized = cv2.equalizeHist(blur)

# -----------------------------
# FEATURE EXTRACTION (GLCM)
# -----------------------------
glcm = graycomatrix(
    equalized,
    distances=[1],
    angles=[0],
    levels=256,
    symmetric=True,
    normed=True
)

contrast = graycoprops(glcm, 'contrast')[0, 0]
energy = graycoprops(glcm, 'energy')[0, 0]
homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]

# -----------------------------
# DISEASE CLASSIFICATION (RULE-BASED)
# -----------------------------
if contrast > 20 and energy < 0.1:
    disease = "PNEUMONIA DETECTED"
elif homogeneity > 0.6:
    disease = "NORMAL CHEST"
else:
    disease = "ABNORMAL - NEEDS CHECKUP"

# -----------------------------
# PRINT RESULTS
# -----------------------------
print("\n========= EXTRACTED FEATURES =========")
print(f"Contrast     : {contrast:.4f}")
print(f"Energy       : {energy:.4f}")
print(f"Homogeneity  : {homogeneity:.4f}")

print("\n========= DIAGNOSIS RESULT =========")
print("Detected Condition:", disease)
print("====================================")

# -----------------------------
# DISPLAY IMAGE & RESULT
# -----------------------------
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f"DETECTION RESULT:\n{disease}", fontsize=14, color="red")
plt.axis("off")
plt.show()
