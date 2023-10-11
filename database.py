import pymssql

### ---- Connect to Database ----- ###
# initialize db and connect to database
def connect_to_database():
    # connect to database
    # Connection details
    server = 'ids706server.database.windows.net'
    port = 1433
    user = 'azureuser'
    password = 'Lilinke@#918918'
    database = 'IDS706Database'

    # Build connection string
    # conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server},{port};DATABASE={database};UID={user};PWD={password}"

    # Try to establish a connection
    # conn = pymssql.connect(server, user, password, database)
    connection = pymssql.connect(server=server, port=port, user=user, password=password, database=database)
    # try:
    #     with pymssql.connect(server=server, port=port, user=user, password=password, database=database) as connection:
    #         print("Connected!")
    # except Exception as e:
    #         print("Failed to connect to the database:", str(e))
    return connection



# create a cursor: a cursor is a database object used to traverse
def create_cursor(connection):
    cursor = connection.cursor()
    return cursor


### ---- CRUD ----- ###
# create a table
def create_table(connection, cursor, query_creation):
    cursor.execute(query_creation)
    connection.commit()


# insert data to the table
def insert_data(cursor, connection, sql_insertion, data_to_insert):
    cursor.execute(sql_insertion, data_to_insert)
    connection.commit()


# read data from table
def read_data(cursor, sql_read, input_read):
    cursor.execute(sql_read, (input_read,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


# update data from table
def update_data(cursor, connection, query_update, stock, name):
    cursor.execute(
        query_update,
        (
            stock,
            name,
        ),
    )
    connection.commit()


# delete data from table
def delete_data(cursor, connection, sql_delete, name2):
    cursor.execute(sql_delete, (name2,))
    connection.commit()


### ---- two more queries ---- ###
def count_book_by_stock(cursor, stock):
    cursor.execute("SELECT COUNT(*) FROM books WHERE stock=?", (stock,))
    return cursor.fetchone()


def fetch_books_ordered_by_name(cursor):
    cursor.execute("SELECT * FROM books ORDER BY name")
    return cursor.fetchall()


def main():
    connection = connect_to_database()
    # create cursor
    cursor = create_cursor(connection)

    # C: create a table
    query_creation = """
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'books')
    BEGIN
        CREATE TABLE books (
            name NVARCHAR(255) NOT NULL,
            stock INT NOT NULL,
            comment NVARCHAR(MAX)
        )
    END
    """
    create_table(connection, cursor, query_creation)

    
    query_insertion = "INSERT INTO books (name, stock, comment) VALUES (@name, @stock, @comment)"

    data1 ={
            'name': 'Red Chamber',
            'stock': 30,
            'comment': 'Uncopiable Love Story'
    }
    insert_data(cursor, connection, query_insertion, data1)
    data2 ={
            'name': 'Educated',
            'stock': 35,
            'comment': 'Meaning of Education'
    }
    insert_data(cursor, connection, query_insertion, data2)
    data3 ={
            'name': 'Utopia',
            'stock': 15,
            'comment': 'A world of democracy imagined by Plato'
    }
    insert_data(cursor, connection, query_insertion, data3)
    data4 ={
            'name': 'Mob',
            'stock': 23,
            'comment': 'Psychological Reflection of the Group'
    }
    insert_data(cursor, connection, query_insertion, data4)
    '''
    # R: read from table
    query_read = "SELECT * FROM books WHERE name=?"
    input_read = "Red Chamber"
    read_data(cursor, query_read, input_read)
    # U: update table
    query_update = "UPDATE books SET stock=? WHERE name=?"
    stock = 25
    name = "Red Chamber"
    update_data(cursor, connection, query_update, stock, name)
    # two more queries
    print(count_book_by_stock(cursor, 35))
    print(fetch_books_ordered_by_name(cursor))
    # D: Delete table
    query_deletion = "DELETE FROM books WHERE name=?"
    name2 = "Red Chamber"
    name3 = "Educated"
    delete_data(cursor, connection, query_deletion, name2)
    delete_data(cursor, connection, query_deletion, name3)

    # close connection
    connection.close()
    '''


if __name__ == "__main__":
    main()
