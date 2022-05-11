from postgres_connector import *
from objects import *
from config import config
from constants import *


def main():
    # Parse database credentials from database.ini via config parser
    database = config('../postgresql/database.ini', 'postgresql')
    # Connect to the database
    connection, cursor = connect(**database)
    # Initialize table in database
    send_from_query(connection, cursor, '../postgresql/create.sql')
    # Sending port-channels to the database
    for key in types['Port-channel']:
        send(connection, cursor, insert, objects[key].get_data())
        print(f'Sending: {objects[key].get_data()}')
    # Request for port_channel_id
    for key in objects.keys():
        id_on_demand = objects[key].id_on_demand
        if id_on_demand:
            send(connection, cursor, select.format(id_on_demand))
            port_channel_id = cursor.fetchall()[0][0]
            objects[key].port_channel_id = port_channel_id
    # Sending ethernet-interfaces to the database
    for key in types:
        if key == 'Port-channel':
            continue
        else:
            for k in types[key]:
                send(connection, cursor, insert, objects[k].get_data())
                print(f'Sending: {objects[k].get_data()}')

    disconnect(connection, cursor)


if __name__ == '__main__':
    main()
