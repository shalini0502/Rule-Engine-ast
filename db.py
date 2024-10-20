import psycopg2

def connect_db():
    conn = psycopg2.connect(
        dbname="rule_engine",
        user="postgres",
        password="shalini", 
        host="localhost"
    )
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rules (
        id SERIAL PRIMARY KEY,
        rule_string TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS metadata (
        id SERIAL PRIMARY KEY,
        attribute_name VARCHAR(255) NOT NULL,
        attribute_type VARCHAR(50) NOT NULL
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()
