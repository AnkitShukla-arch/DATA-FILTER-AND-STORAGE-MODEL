import os
import shutil
import logging

logger = logging.getLogger(__name__)

def safe_makedirs(path):
    """Safely create a directory like 'mkdir -p'."""
    try:
        os.makedirs(path, exist_ok=True)
        logger.info(f"✅ Directory ensured: {path}")
        return True
    except Exception as e:
        logger.error(f"❌ Error creating directory {path}: {e}")
        return False

def safe_remove(path):
    """Safely remove a file or directory if it exists."""
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        logger.info(f"🗑️ Removed: {path}")
        return True
    except Exception as e:
        logger.error(f"❌ Error removing {path}: {e}")
        return False
