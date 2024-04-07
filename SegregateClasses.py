import os
import shutil
import pandas as pd

csv_file = "E:/IISC academics/SEM- 2/DS-216 Machine learning for data science/Assignments/Assignment 2/ASSN2_Q2/train.csv"
data = pd.read_csv(csv_file)
source_folder = "E:/IISC academics/SEM- 2/DS-216 Machine learning for data science/Assignments/Assignment 2/ASSN2_Q2/train"
output_folder = "E:/IISC academics/SEM- 2/DS-216 Machine learning for data science/Assignments/Assignment 2/ASSN2_Q2/classified"
healthy_dir = os.path.join(output_folder, "0")
diseased_dir = os.path.join(output_folder, "1")
os.makedirs(healthy_dir, exist_ok=True)
os.makedirs(diseased_dir, exist_ok=True)
for index, row in data.iterrows():
    image_filename = row["id"]
    class_label = row["binary_pred"]
    source_path = os.path.join(source_folder, image_filename)
    if class_label == 0:
        target_path = os.path.join(healthy_dir, image_filename)
    elif class_label == 1:
        target_path = os.path.join(diseased_dir, image_filename)
    shutil.copy(source_path, target_path)
