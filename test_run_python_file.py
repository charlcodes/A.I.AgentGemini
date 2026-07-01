from functions.run_python_file import run_python_file


test0 = run_python_file("calculator", "main.py") #(should print the calculator's usage instructions)
test1 = run_python_file("calculator", "main.py", ["3 + 5"]) #(should run the calculator... which gives a kinda nasty rendered result)
test2 = run_python_file("calculator", "tests.py") #(should run the calculator's tests successfully)
test3 = run_python_file("calculator", "../main.py") #(this should return an error)
test4 = run_python_file("calculator", "nonexistent.py") #(this should return an error)
test5 = run_python_file("calculator", "lorem.txt") #(this should return an error)

for i in range(0, 6):
    variable_name = f"test{i}"
    value = locals()[variable_name]
    print(value)