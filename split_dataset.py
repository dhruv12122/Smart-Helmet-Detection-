import os, random, shutil

IMG_DIR = "img"
LABEL_DIR = "labels_yolo"
OUT_DIR = "final_dataset"

#Output folders
for split in ["train", "val"]:
    os.makedirs(os.path.join(OUT_DIR, "images", split), exist_ok=True)
    os.makedirs(os.path.join(OUT_DIR, "labels", split), exist_ok=True)

# image list
images = [f for f in os.listdir(IMG_DIR) if f.endswith((".jpg", ".png"))]
random.shuffle(images)

split_idx = int(len(images) * 0.8)
train_imgs, val_imgs = images[:split_idx], images[split_idx:]

def move_files(img_list, split):
    copied, skipped = 0, 0
    for img in img_list:
        label = img.rsplit(".", 1)[0] + ".txt"
        label_path = os.path.join(LABEL_DIR, label)
        if not os.path.exists(label_path):
            skipped += 1
            continue
        shutil.copy(os.path.join(IMG_DIR, img), os.path.join(OUT_DIR, "images", split, img))
        shutil.copy(label_path, os.path.join(OUT_DIR, "labels", split, label))
        copied += 1
    print(f"Split '{split}': copied {copied}, skipped {skipped}")

move_files(train_imgs, "train")
move_files(val_imgs, "val")
print("✅ Dataset split finished!")