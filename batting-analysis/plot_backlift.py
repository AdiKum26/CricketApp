import os
import pandas as pd
import matplotlib.pyplot as plt

pose_dir = "pose_data"
output_dir = "backlift_plots"
os.makedirs(output_dir, exist_ok=True)

def plot_backlift(csv_file):
    df = pd.read_csv(os.path.join(pose_dir, csv_file))
    wrist_y = df["y16"]
    shoulder_y = df["y12"]
    backlift_height = shoulder_y - wrist_y

    plt.figure(figsize=(10, 5))
    plt.plot(backlift_height, label="Backlift Height (shoulder_y - wrist_y)", color='blue')
    plt.axhline(0.02, color='green', linestyle='--', label="Ideal Lower Bound")
    plt.axhline(0.08, color='green', linestyle='--', label="Ideal Upper Bound")
    plt.title(f"Backlift Over Time - {csv_file}")
    plt.xlabel("Frame")
    plt.ylabel("Backlift Height")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save plot
    plot_path = os.path.join(output_dir, f"{csv_file[:-4]}_backlift.png")
    plt.savefig(plot_path)
    plt.close()

for file in os.listdir(pose_dir):
    if file.endswith(".csv"):
        print(f"📊 Plotting: {file}")
        plot_backlift(file)

print("✅ All plots generated in 'backlift_plots/' folder.")