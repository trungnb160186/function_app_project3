import logging
import psycopg2
from azure.functions import ServiceBusMessage


def main(msg: ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))
    
    # Update connection string information
    host = "<server-name>"
    dbname = "<database-name>"
    user = "<admin-username>"
    password = "<admin-password>"
    sslmode = "require"

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
