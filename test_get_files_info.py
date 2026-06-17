from functions.get_files_info import get_files_info

test0 = get_files_info("calculator", ".")
test1 = get_files_info("calculator", "pkg")
test2 = get_files_info("calculator", "/bin")
test3 = get_files_info("calculator", "../")
#test4 = get_files_info("calculator", "main.py")
print(f"{test0}\n{test1}\n{test2}\n{test3}") #\n{test4}