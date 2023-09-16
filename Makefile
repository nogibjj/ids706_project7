# Setup virtual environment
setup:
	python3 -m venv env
	# source env/bin/activate

# Install dependencies
install:
	./env/bin/pip install -r requirements.txt

# Lint the project
lint:
	# ./env/bin/flake8 -v . > my_log.txt
	# ./env/bin/flake8 /home/ll442/ids706/hw2/ids706_hw2/describe_statistics.py > my_log.txt
	./env/bin/pylint --disable=R,C --ignore-patterns=test_.*?py *.py

# check the format
format:	
	./env/bin/black *.py 

# Run tests
test:
	./env/bin/python3 -m pytest -vv test_*.py
	# ./env/bin/pytest

# Run your script (replace 'your_script_name.py' with the actual script name)
run:
	./env/bin/python3 describe_statistics.py

# Command to do everything: setup, install, lint, test and run
all: setup install lint format test run
