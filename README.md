# ids706_python_template
Individual Project1 for ids706: 
- Python Script interacting with SQL Database


## Requirements
- Python 3.8+
- Virtual environment (optional but recommended, already set up as env in Makefile)
- Packages listed in `requirements.txt` including 


## Set up
1. Run `make setup` to set up the virtual environment for the project.
note: only need to set up the environment once
2. Run `make install` to install all packages listed in requirement.txt
3. Run `make lint` to check up the style
4. Run `make format` to check up the format
5. Run `make test` to test the main.py
6. Run `make all` to finish all the badges at the same time


## Database Interaction
- In this project, SQL operations including **database connection**, **CRUD operations**, and **several other SQL queries** are written in `database.py`. 
1. Connect to Database 
`connect_to_database(db)`,`create_cursor(connection)` are important functions for database connection
2. CRUD operations
**CREATE**: Create Table with:`create_table`, and Insert data to the table with `insert_data`
**READ**: Read data from the Table with `read_data`
**UPDATE**: Update data in the table with `update_data`
**Delete**: Delete data from the table with `delete_data`
3. Two other queries:
**count_book_by_stock**: Return the number of books of certain number of stock with `count_book_by_stock`
**fetch_books_ordered_by_name**: Return the books ordered by book name with `fetch_books_ordered_by_name`


- To test the SQL operations written in database.py, you should follow the following steps:
1. Since all packages are downloaded to the virtual environment `.env`, activate the virtual environment with `source env/bin/activate`
2. Run `python3 database.py` or `python3 database.py > output.log` to write all the output related with the SQL operations to terminal or output.log file
3. check the terminal or output.log for result


## Structure
1. `.devcontainer` includes a Dockerfile and devcontainer.json. The files in this container specify how the project can be set up.
2. `.github` includes the CI/CD settings
3. `database.py` includes all the operations related with SQL
4. `Makefile` includes all the make settings for this project
5. `book.db` is the database we will operate on
6. `test_main.py` is the test file for `main.py`
7. All packages needed for this project are in `requirements.txt`
8. `.gitignore` includes all the files that do not want to be tracked by github


## CI/CD
GitHub Actions are configured for Continuous Integration and Continuous Deployment. See `.github/workflows/ci_cd.yml` for details.




