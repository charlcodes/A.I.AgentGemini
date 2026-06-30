import os
from pathlib import Path
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        abs_pth_wrk_dir: str = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(abs_pth_wrk_dir, file_path))
        valid_target_dir: bool = os.path.commonpath([abs_pth_wrk_dir, target_file]) == abs_pth_wrk_dir
    except Exception as e:
        return f'Error: {e}'
    
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not Path(target_file).is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(target_file, mode="r", encoding="utf-8") as file:
        content = file.read(MAX_CHARS)
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return content    