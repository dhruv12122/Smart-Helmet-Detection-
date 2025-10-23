# 👷 Smart Safety Helmet Detection and Voice Alert System

## 🌟 Project Overview

This project implements a real-time computer vision system designed to enhance safety in industrial or construction environments. It uses state-of-the-art object detection to monitor personnel and automatically issues a spoken safety warning if an individual is detected **not wearing a helmet**.

The core system is built upon the **YOLOv11 Nano (YOLOv11n)** model, which provides a fast and highly efficient solution suitable for live video streams and edge deployment.

### 🎯 Key Features

* **Real-Time Detection:** Processes live video streams (webcam or IP camera) for immediate safety monitoring.
* **High Accuracy:** Achieves a **94.0% Mean Average Precision (mAP@50)** on the validation dataset.
* **Automated Voice Alert:** Triggers a pre-recorded audio warning ("Attention! Wear the helmet for your safety.") via the computer's speaker when a `no_helmet` instance is confidently detected.
* **Efficient Model:** Utilizes the lightweight **YOLOv11n** model for optimal speed and resource efficiency.

***
| Metric | Value | 
| :--- | :--- | 
| **All Classes mAP@0.5** | **0.940** | 
| Helmet Precision | 0.956 | 
| No-Helmet Precision | 0.924 |

## ⚙️ Technical Details

| File Name | Description | 
| :--- | :--- | 
| **`correction.py`** | **Annotation Correction Utility.** A script likely used to correct or clean up initial dataset annotations, paths, or class indices before final conversion. | 
| **`json_to_yolo.py`** | **Annotation Conversion Script.** Converts raw annotations (e.g., JSON or XML format) from the initial annotation tool into the simple, plain-text YOLO format (`.txt` files) required for training. | 
| **`split_dataset.py`** | **Data Management Script.** Used to randomly split the complete set of images and corresponding labels into `train`, `val` (validation), and `test` subdirectories for model training. |



| Component | Value/Version | Purpose |
| :--- | :--- | :--- |
| **Model Architecture** | YOLOv11n | High-performance, low-latency object detection. |
| **Framework** | Ultralytics (YOLO) | Training and Inference framework. |
| **Training Data** | Custom Dataset (Helmet/No-Helmet) | Total instances: 19,666 (15,091 helmet, 4,575 no-helmet) |
| **Final Performance**| **mAP@50: 0.940** | Overall detection accuracy. |
| **Software** | Python 3.10, PyTorch 2.5.1, OpenCV | Core programming and deep learning libraries. |
| **Hardware** | NVIDIA GeForce RTX 2050 (4GB VRAM) | Training was performed with full GPU acceleration. |

***

## 🚀 Setup and Installation

### 1. Prerequisites

Ensure you have a modern NVIDIA GPU and the appropriate drivers installed, along with **CUDA (v12.1 or newer)** for GPU acceleration.

### 📥 Dataset Access
Due to its large size, the custom dataset is not included in the repository.

* **Download Link:** https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection

### 2. Environment Setup

```bash
# Clone the repository (if hosted on Git)
# git clone <repository_url>
# cd <project_directory>

# Create and activate a Python virtual environment (recommended)
python -m venv venv
.\venv\Scripts\activate  # On Windows PowerShell
# source venv/bin/activate # On Linux/macOS

# Install required packages
pip install ultralytics torch==2.5.1+cu121 torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)
pip install opencv-python playsound gTTS
