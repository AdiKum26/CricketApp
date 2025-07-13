import cv2
import mediapipe as mp
import os
import csv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False)
video_dir = "videos"
output_dir = "pose_data"
os.makedirs(output_dir, exist_ok=True)

def extract_pose_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    data = []
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(frame_rgb)
        if result.pose_landmarks:
            landmarks = result.pose_landmarks.landmark
            row = []
            for lm in landmarks:
                row.extend([lm.x, lm.y, lm.z, lm.visibility])
            data.append(row)
    cap.release()
    return data

for shot_type in os.listdir(video_dir):
    shot_folder = os.path.join(video_dir, shot_type)
    if not os.path.isdir(shot_folder): continue

    for filename in os.listdir(shot_folder):
        if not filename.endswith(".mp4"):
            continue
        filepath = os.path.join(shot_folder, filename)
        print(f"Processing {filepath}...")
        pose_data = extract_pose_from_video(filepath)
        output_csv = os.path.join(output_dir, f"{shot_type}_{filename[:-4]}.csv")

        with open(output_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            # 33 keypoints x (x, y, z, visibility)
            header = []
            for i in range(33):
                header += [f"x{i}", f"y{i}", f"z{i}", f"v{i}"]
            writer.writerow(header)
            writer.writerows(pose_data)

print("✅ All pose data extracted!")