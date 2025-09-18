# 🏏 CricketApp – Batting Technique Analysis with AI & Pose Estimation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/AdiKum26/CricketApp)

CricketApp is a machine learning project designed to **analyze cricket batting techniques** — specifically the **backfoot defense** — using pose estimation and data comparison. The goal is to provide **coaches and players** with feedback by comparing a player’s movements to **ideal batting data**.

---

## 📂 Project Structure

```
CricketApp/
│── batting-analysis/         # Core analysis scripts
│   ├── analyze_backlift.py   # Analyze bat backlift from pose data
│   ├── extract_backfoot_defence.py # Extract batting frames for backfoot defense
│   ├── extract_poses.py      # Pose extraction from video using ML models
│   ├── plot_backlift.py      # Generate graphs for batting angles/backlift
│   ├── visualize_pose_video.py # Overlay pose landmarks on cricket video
│   ├── requirements.txt      # Python dependencies
│   └── .gitignore
│
│── ideal_backfoot_data/      # Ground truth CSVs with ideal batting poses
│   ├── 1_ideal.csv
│   ├── 2_ideal.csv
│   ├── 3_ideal.csv
│   ├── 4_ideal.csv
│   └── 5_ideal.csv
│
└── README.md                 # Project documentation
```

---

## 🚀 Features

- **Pose Extraction**: Capture player movement frame-by-frame from cricket videos.
- **Backfoot Defense Analysis**: Extracts batting-specific frames and compares them with ideal data.
- **Bat Backlift Analysis**: Quantifies and visualizes the angle and position of the bat during stance and defense.
- **Pose Visualization**: Generates annotated videos with pose landmarks for easier feedback.
- **Data Comparison**: Uses CSV-based reference data of ideal techniques for benchmarking.

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/AdiKum26/CricketApp.git
cd CricketApp/batting-analysis
pip install -r requirements.txt
```

---

## 🏃 Usage

### 1. Extract Pose Data
```bash
python extract_poses.py --input your_video.mp4 --output poses.json
```

### 2. Analyze Backfoot Defense
```bash
python extract_backfoot_defence.py --poses poses.json --output defence.csv
```

### 3. Compare with Ideal Data
```bash
python analyze_backlift.py --input defence.csv --ideal ../ideal_backfoot_data/1_ideal.csv
```

### 4. Visualize Pose on Video
```bash
python visualize_pose_video.py --input your_video.mp4 --poses poses.json --output annotated_video.mp4
```

---

## 📊 Example Workflow

1. Record a cricket batting video (backfoot defense shot).  
2. Extract pose landmarks using `extract_poses.py`.  
3. Run analysis scripts to evaluate bat backlift and compare player’s technique with ideal reference data.  
4. Generate annotated visualizations and performance metrics.  

---

## 📈 Applications

- Coaching aid for **grassroots cricket training** 🏏  
- Performance analysis for **semi-professional players**  
- Research into **sports biomechanics & pose estimation**  
- Foundation for a **mobile cricket coaching app**  

---

## 🛠️ Tech Stack

- **Python** (core language)  
- **OpenCV** for video processing  
- **Pose Estimation Models** (MediaPipe / OpenPose)  
- **Pandas, NumPy, Matplotlib** for data analysis & visualization  

---

## 📌 Future Improvements

- Expand analysis beyond backfoot defense (cover drives, pull shots, etc.)  
- Build a **real-time mobile coaching app** with pose feedback  
- Integrate with **deep learning models** for automated classification  
- Cloud-based dashboard for storing and reviewing player sessions  

---

## 👨‍💻 Authors

- **Aditya Kumar**  
- **Akshith Saravanan**  

---

> ⚡ *Cricket + AI = Smarter Coaching. This project is our step towards blending sports and technology to help players improve their game.*
