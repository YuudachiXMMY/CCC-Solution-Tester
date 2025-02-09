# CCC Solution Tester

This is a solution tester for University of Waterloo CCC (Canadian Computing Competition) in Python.

You can find all of contest related information and practice at <https://dmoj.ca> and <https://cemc.uwaterloo.ca>.

## Setting-Up

### For File Directories

Make sure your directory structure match the following:

```text
/SOME_FOLDER/
    - runTest.py    [THIS PROGRAM]
    - s1.py         [Your solution to s1]
    - s2.py         [Your solution to s2]
    - /all_data/
        - /s1
            - SOME_TEST_CASE_1.in
            - SOME_TEST_CASE_1.out
        - /s2/
            - SOME_TEST_CASE_1.in
            - SOME_TEST_CASE_1.out
```

You can feel free to change the folder name `/all_data/` but make sure you also change the variable name `TEST_DATA_DIR` on the 12th line in the `tester.py`.

### For Solution Programs

In your solution files (E.g. `s1.py`, `s2.py`), make sure the coding structure follows:

```python
def solution():
    # Your Solution to the problem
    print('Expected Outputs')

def run():
    solution()

if __name__ == '__main__':
    run()
    # CCCs_test.test("s2")
```

## Usage

To run the tests, your **terminal working directory** must be the same as **solution directory**.

In the [case above](#for-file-directories), your terminal directory should be **`/SOME_FOLDER/`**.

Running test in the terminal for `s1`:

```bash
python runTest.py s1
```
