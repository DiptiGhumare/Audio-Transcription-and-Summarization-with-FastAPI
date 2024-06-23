import os
import json

def save_transcription(transcription, save_dir, filename, timestamp):
    try:
        file_name = f"{filename.split('.')[0]}_transcription_{timestamp}.txt"
        file_path = os.path.join(save_dir, file_name)

        with open(file_path, "w") as f:
            f.write(transcription)

    except Exception as e:
        raise RuntimeError(f"Error saving transcription: {str(e)}")

def save_summary(summary, save_dir, filename, timestamp):
    try:
        file_name = f"{filename.split('.')[0]}_summary_{timestamp}.txt"
        file_path = os.path.join(save_dir, file_name)

        with open(file_path, "w") as f:
            f.write(summary)

    except Exception as e:
        raise RuntimeError(f"Error saving summary: {str(e)}")

def save_timestamps(timestamps, save_dir, filename, timestamp):
    try:
        file_name = f"{filename.split('.')[0]}_timestamps_{timestamp}.json"
        file_path = os.path.join(save_dir, file_name)

        with open(file_path, "w") as f:
            json.dump(timestamps, f)

    except Exception as e:
        raise RuntimeError(f"Error saving timestamps: {str(e)}")
