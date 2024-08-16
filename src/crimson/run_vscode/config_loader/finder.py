import os
from typing import Optional


def find_closest_file(file_name: str) -> Optional[str]:
    """Search for the closest file in the current or parent directories."""
    current_dir = os.getcwd()
    while current_dir != os.path.dirname(current_dir):
        potential_path = os.path.join(current_dir, file_name)
        if os.path.exists(potential_path):
            return potential_path
        current_dir = os.path.dirname(current_dir)
    return None


def find_closest_dir(dir_name: str) -> Optional[str]:
    """Search for the closest directory in the current or parent directories."""
    current_dir = os.getcwd()
    while current_dir != os.path.dirname(current_dir):
        potential_path = os.path.join(current_dir, dir_name)
        if os.path.isdir(potential_path):
            return potential_path
        current_dir = os.path.dirname(current_dir)
    return None
