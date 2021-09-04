# Getting Started with MiniCarwale



## Installing the dependencies

To run the program, you would require any IDE
- [VS code](https://code.visualstudio.com/download) - Install python Extension in VS code 
- [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) - Configure a Python interpreter in PyCharm 
 

## Running the program

1. Once you have downloaded the dependencies required, clone this github repository.
2. Next, Open up the terminal console and run the `python3 main.py` command in the terminal.

   The program is now compiled and ready to run! :tada:
## To run pytest
```
pip install pytest
```
1. Install pytest package and run `pytest -v .` for testing all testcases

![](https://github.com/barathjk/MiniCarwale/blob/main/5_ImagesandVideos/Pytest.jpeg)

## To run pylint
```
pip install pylint
```
1. Install pylint package and run `pytest main.py` for main file
2. To run pylint for all .py files go back to parent directory `cd ..` and run `pylint cd 4_implementation`

![](https://github.com/barathjk/MiniCarwale/blob/main/5_ImagesandVideos/Pylint%20Score%20for%20all%20py%20files.jpeg)
## Advanced Guide
- `carclass.py` - Contains Hierarchical Inheritance
- `cars.py`- Choose between cars
- `data.txt` - Login details storage
- `emicalc.py` - Calculate Equated Monthly Installment
- `main.py` - main file
- `test_emicalc.py` - test file for minicarwale
