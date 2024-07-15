# CCC Solution Tester

This is a solution tester for University of Waterloo CCC (Canadian Computing Competition) in Python.

You can find all of contest related problems at <https://dmoj.ca> or <https://cemc.uwaterloo.ca>.

## Usage

1. Make sure your directory structure match the following:

    ```text
    /SOME_FOLDER/
        - tester.py     [THIS PROGRAM]
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

2. To run the tests, make sure your terminal working directory matches your solutions and the tester files' directory. In the case above, it should be `/SOME_FOLDER/`

3. Run test in the terminal:

```bash
python tester.py s1
```
