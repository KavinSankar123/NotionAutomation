import psycopg2


class PostgreSQLConnection:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="<postgres auth password>"
    )
