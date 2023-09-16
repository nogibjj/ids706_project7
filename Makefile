# Setup virtual environment
setup:
	python3 -m venv env

# Install dependencies
install:
	./env/bin/pip install -r requirements.txt

# Lint the project
lint:
	./env/bin/flake8 -v .

# Run tests
test:
	./env/bin/pytest

# Run your script (replace 'your_script_name.py' with the actual script name)
run:
	./env/bin/python your_script_name.py

# Command to do everything: setup, install, lint, test and run
all: setup install lint test run
