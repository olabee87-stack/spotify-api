import sqlalchemy
import sqlite3
from sqlalchemy.orm import sessionmaker

DATABASE_LOCATION = 'sqlite:///pasta_dishes.sqlite'


def load_data(df):
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('pasta_dishes.sqlite')
    cursor = conn.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS pasta_dishes(
    title: VARCHAR(300),
    nutrition: FLOAT(5, 2),
    CONSTRAINT primary_key_constraint PRIMARY KEY INT AUTO_INCREMENT
    )
    """

    cursor.execute(sql_query)
    print('Database successfully mounted')

    try:
        df.to_sql('pasta_dishes', engine, index=False, if_exists='append')
    except:
        print('Data already exists in the database')

    conn.close()
    print('Database successfully closed')

