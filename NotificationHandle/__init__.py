import logging
import psycopg2
import os
from azure.functions import ServiceBusMessage


def main(msg: ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    
    # Update connection string information
    host = os.environ["DB_HOT"]
    dbname = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PW"]
    sslmode = "require"

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.attendee;")
    attendees =  cursor.fetchall()
    for attendee in attendees:
        print(attendee)
