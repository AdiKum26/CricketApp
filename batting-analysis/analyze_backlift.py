import os
import pandas as pd

pose_dir = "pose_data"

def classify_backlift(avg_height):
    if avg_height < 0.02:
        return "Too Low"
    elif avg_height < 0.08:
        return "Ideal"
    else:
        return "Too High"

for file in os.listdir(pose_dir):
    if not file.endswith(".csv"):
        continue

    df = pd.read_csv(os.path.join(pose_dir, file))

    # Get y-values for right wrist (landmark 16) and right shoulder (landmark 12)
    wrist_y = df["y16"]
    shoulder_y = df["y12"]

    # Backlift height = shoulder_y - wrist_y
    backlift_height = shoulder_y - wrist_y

    avg_backlift = backlift_height.mean()
    max_backlift = backlift_height.max()
    label = classify_backlift(avg_backlift)

    print(f"\n📂 {file}")
    print(f"• Avg Backlift Height: {avg_backlift:.4f}")
    print(f"• Max Backlift Height: {max_backlift:.4f}")
    print(f"• Classification: {label}")