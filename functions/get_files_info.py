import os
from pathlib import Path
from google.genai import types

def get_files_info(working_directory: str, directory: str = ".") -> str:
    """path validation"""
    try:
        abs_pth_wrk_dir: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(abs_pth_wrk_dir, directory))
        is_within_working_dir: bool = os.path.commonpath([abs_pth_wrk_dir, target_dir]) == abs_pth_wrk_dir
    except Exception as e:
        return f'Error: {e}'
        
    if not is_within_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not Path(target_dir).is_dir():
        return f'Error: "{directory}" is not a directory'
    
    #if success
    else:
        #return f'Success: "{directory}" is within the working directory'
        #dir_path = Path(directory)
        #for item in dir_path.iterdir():
        items_in_dir = []
        try:
            for entry in os.scandir(target_dir):
                items_in_dir.append(f"  - {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}")
            return f"Result for {'current' if directory == '.' else directory} directory:\n" + '\n'.join(items_in_dir)

        except Exception as e:
            return f'Error: {e}'


"""Schema_Declaration"""

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

