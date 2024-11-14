from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os 

def configure():
    load_dotenv()

db_connection_string = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dicts = [row._asdict() for row in result.all()]  # Using _asdict() method

    print(result_dicts)

def load_jobs_from_db():
    with engine.connect() as conn:  # Correct indentation for the `with` block
        result = conn.execute(text("select * from jobs"))
        result_dicts = [row._asdict() for row in result.all()]  # Using _asdict() method
    return result_dicts  # Correct return statement
