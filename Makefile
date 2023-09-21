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
	./env/bin/python -m pytest test_script.py 
	./env/bin/python -m pytest test_lib.py
	./env/bin/python -m pytest descriptive_stats.ipynb --nbval
	
		
all: setup install lint format test 