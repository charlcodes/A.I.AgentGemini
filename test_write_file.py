from unittest import result

from functions.write_file import write_file

file_path_content = [
    ("lorem.txt", "wait, this isn't lorem ipsum"),
    ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("/tmp/temp.txt", "this should not be allowed")
]
for fp, c in file_path_content:
    result = write_file("calculator", fp, c)
    print(result)