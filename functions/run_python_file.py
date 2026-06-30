from ast import And
import subprocess
import os
from pathlib import Path

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    
    try:
       abs_pth_wrk_dir: str = os.path.abspath(working_directory)
       target_file: str = os.path.normpath(os.path.join(abs_pth_wrk_dir, file_path))
       is_within_working_dir: bool = os.path.commonpath([abs_pth_wrk_dir, target_file]) == abs_pth_wrk_dir

   
    
       if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
       if not is_within_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
       if not Path(target_file).is_file():
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        
       command: list[str] = ["python", target_file] # absolute_file_path?
       command.extend(args or [])
       completion_obj: subprocess.CompletedProcess[str] = subprocess.run(command, capture_output= True, text= True, cwd = abs_pth_wrk_dir, timeout= 30) #not sure if build the return string from completion_obj.stdout, completion_obj.stderr, and completion_obj.returncode
       return_string: str = ""


       output_parts: list[str] = []

       if completion_obj.returncode != 0:
            output_parts.append(f"Process exited with code {completion_obj.returncode}")

       if not completion_obj.stdout and not completion_obj.stderr:
            output_parts.append("No output produced")
       else:
            if completion_obj.stdout:
                output_parts.append(f"STDOUT: {completion_obj.stdout}")
            if completion_obj.stderr:
                output_parts.append(f"STDERR: {completion_obj.stderr}")

       return "\n".join(output_parts)
       '''if completion_obj.check_returncode != 0:
           error_code_str:str =f"Process exited with code {completion_obj.check_returncode}"
       if completion_obj.stdout == "" and completion_obj.stderr == "":
          '''  
    except Exception as e:
        return f'Error: {e}'