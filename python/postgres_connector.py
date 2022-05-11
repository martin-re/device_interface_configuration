import psycopg2

'''This module is helper for main.py.
The module contains a few functions handling connection to postgres database.'''


def connect(host, dbname, user, password, port):
    connection, cursor = None, None
    try:
        connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        cursor = connection.cursor()
        print(f"Connecting to the {dbname} database ...", end='\n')
        return connection, cursor
    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def send(connection, cursor, command, values=None):
    try:
        if values is None:
            cursor.execute(command)
        else:
            cursor.execute(command, values)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def disconnect(connection, cursor):
    try:
        cursor.close()
        connection.close()
        print('Disconnecting ...')
    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def send_from_query(connection, cursor, file):
    try:
        with open(file, 'r') as f:
            send(connection, cursor, f.read())
    except FileNotFoundError:
        print(f"{file} doesn't exist")
