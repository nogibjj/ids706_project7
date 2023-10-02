# Setup virtual environment
setup:
	python3 -m venv env
	# source env/bin/activate

# install all the packages
install:
	./env/bin/pip install --upgrade pip &&\
		./env/bin/pip install -r requirements.txt

lint:
	./env/bin/ruff check --fix .

format:	
	./env/bin/black *.py 

test:
	./env/bin/python -m pytest test_main.py 
	
		
all: setup install lint format test 