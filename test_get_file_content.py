from functions.get_file_content import get_file_content

#print(f"lorem.txt length: {len(result)}")
#print(f"lorem.txt truncated: {'truncated' in result}")

files = [
    "lorem.txt",
    "main.py",
    "pkg/calculator.py",
    "/bin/cat",
    "pkg/does_not_exist.py",
]

for file in files:
    result = get_file_content("calculator", file)
    print(f"{file} lenth: {len(result)}\n{file} truncated: {'truncated' in result}\n\n{result}\n")