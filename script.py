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

main_path = pathlib.Path('main.py')
main_content = main_path.read_text()

for i in range(1, n_tests + 1):
    test_path = pathlib.Path(tests) / str(i)
    clue_path = pathlib.Path(tests) / f'{str(i)}.clue'
    with test_path.open() as test, clue_path.open() as clue:
        combined_content = main_content + '\n' + '\n' + '\n' + test.read()
        combined_path = pathlib.Path('combined_main.py')
        combined_path.write_text(combined_content)

        result = os.popen(f"{python_version} {combined_path} < {test_path}").read().strip()
        correct = clue.read()
        assert result == correct, f"Test#{i}\n{'-' * 69}\nexpect:{repr(correct)}\nresult:{repr(result)}\n"
    print(f'Test#{i} PASSED')
print(f'Everything is fine! {n_tests} pieces checked.')

combined_path.unlink()