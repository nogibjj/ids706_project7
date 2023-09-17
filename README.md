# ids706_python_template
Week3 homework for ids706: 
- Write a script to read dataset Book.xlsx, visualize the data and generate the pdf report with polars library

## Requirements

- Python 3.8+
- Virtual environment (optional but recommended)
- Packages listed in `requirements.txt`

## Setup and Check Format
1. Clone the repository
2. cd to the directory: ~/ids706_week3_MiniProject_LinkeLi
3. Run `make setup` to set up the virtual environment
4. Run `make install` to install all the packages needed as shown in requirement
- polars==0.10.26 to ensure that the program functions well
5. Run `make lint` to check up the style
6. Run `make format` to check up the format
7. Run `make test` to test the code with pylint and the test cases in test_stat.py
you can add more test cases in test_stat.py

## Useage
8. Run `make run` to generate data visualization and report to ~/ids706_week3_MiniProject_LinkeLi

- To combine step 3~8 as stated above, you can run `make all` directly


## CI/CD
GitHub Actions are configured for Continuous Integration and Continuous Deployment. See `.github/workflows/ci_cd.yml` for details.


