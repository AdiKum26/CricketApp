import cv2
import mediapipe as mp
import os
import csv

# Landmarks to extract
landmark_indices = [0, 11, 12, 13, 14, 15, 16, 23, 24, 25, 26, 27, 28]

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

video_folder = "batting-analysis/videos/Backfoot_Defense"
output_folder = 'ideal_backfoot_data'
os.makedirs(output_folder, exist_ok=True)

def extract_selected_landmarks(video_path):
    cap = cv2.VideoCapture(video_path)
    data = []

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(frame_rgb)

        if result.pose_landmarks:
            row = []
            for idx in landmark_indices:
                lm = result.pose_landmarks.landmark[idx]
                row.extend([lm.x, lm.y, lm.z, lm.visibility])
            data.append(row)

    cap.release()
    return data

for filename in os.listdir(video_folder):
    if not filename.endswith(".mp4"):
        continue

    filepath = os.path.join(video_folder, filename)
    print(f"📹 Processing: {filename}")
    pose_data = extract_selected_landmarks(filepath)

    output_csv = os.path.join(output_folder, f"{filename[:-4]}_ideal.csv")
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        header = []
        for idx in landmark_indices:
            header += [f"x{idx}", f"y{idx}", f"z{idx}", f"v{idx}"]
        writer.writerow(header)
        writer.writerows(pose_data)

print("✅ Extracted selected landmark data from all backfoot defense videos.")