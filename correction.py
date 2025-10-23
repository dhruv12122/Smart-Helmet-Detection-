import os

LABEL_DIR = "labels_yolo"

for file in os.listdir(LABEL_DIR):
    if file.endswith(".png.txt"):
        new_name = file.replace(".png.txt", ".txt")
        os.rename(os.path.join(LABEL_DIR, file), os.path.join(LABEL_DIR, new_name))
        print(f"{file} -> {new_name}")

print("succesful!")