# script.py
import os
import pathlib
from sys import platform

DIR = pathlib.Path(__file__).parent.resolve()  # current directory
tests = os.path.join(DIR, 'tests')
try:
    n_tests = len(os.listdir(tests)) // 2  # check if there is a tests folder and a 'main.py' file
    open('main.py')
except FileNotFoundError as error:
    print('-' * 69, '\nERROR 404')
    print('The folder with the tests should be called - tests, and the file with the code - main.py', '-' * 69,
          sep='\n')
    raise

if platform == "linux" or platform == "linux2":  # select the Python version depending on the OS
    python_version = 'python3'
elif platform == "darwin":
    python_version = 'python3'
elif platform == "win32":
    python_version = 'py'

for i in range(1, n_tests + 1):
    with open(os.path.join(tests, str(i))) as test, open(os.path.join(tests, f'{str(i)}.clue')) as clue:
        result = os.popen(f"{python_version} main.py < {os.path.join(tests, str(i))}").read().strip()
        correct = clue.read()
        assert result == correct, f"Test#{i}\n{'-' * 69}\nexpect:{repr(correct)}\nresult:{repr(result)}\n"
    print(f'Test#{i} PASSED')
print(f'Everything is fine! {n_tests} pieces checked.')
