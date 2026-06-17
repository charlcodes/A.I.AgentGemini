import os
from pathlib import Path

def get_files_info(working_directory: str, directory: str = ".") -> str:
    """ os.path.abspath(): Get an absolute path from a relative path
        os.path.join(): Join two paths together safely (handles slashes)
        os.path.normpath(): Normalize a path (handles things like ..)
        os.path.commonpath(): Get the common sub-path shared by multiple paths
        os.path.isdir(): Check if a path points to an existing directory 
    """

    """path validation"""
    try:
        abs_pth_wrk_dir: str = os.path.abspath(working_directory)
        target_dir: str = os.path.normpath(os.path.join(abs_pth_wrk_dir, directory))
        valid_target_dir: bool = os.path.commonpath([abs_pth_wrk_dir, target_dir]) == abs_pth_wrk_dir
    except Exception as e:
        return f'Error: {e}'
        
    if not valid_target_dir:
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
    



