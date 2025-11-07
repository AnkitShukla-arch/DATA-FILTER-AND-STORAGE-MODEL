import os
import shutil

def safe_makedirs(path):
    """
    Safely create a directory if it doesn't already exist.
    Works like 'mkdir -p' in Linux.
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✅ Directory ensured: {path}")
    except Exception as e:
        print(f"❌ Error creating directory {path}: {e}")

def safe_remove(path):
    """
    Safely remove a file or directory if it exists.
    """
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        print(f"🗑️ Removed: {path}")
    except Exception as e:
        print(f"❌ Error removing {path}: {e}")
