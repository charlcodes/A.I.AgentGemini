import os
from pathlib import Path

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_pth_wrk_dir: str = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(abs_pth_wrk_dir, file_path))
        is_within_working_dir: bool = os.path.commonpath([abs_pth_wrk_dir, target_file]) == abs_pth_wrk_dir
    
        if not is_within_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if Path(target_file).is_dir():
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        #os.makedirs(target_file, exist_ok=True) # i did not like this
    
        target = Path(target_file)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    #with open(target_file, mode="w", encoding="utf-8") as file:
    #    file.write(content)
    
    