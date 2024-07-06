import logging
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import configparser

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_snowflake_connection(config):
    """
    Create and return a Snowflake connection using credentials from the config file.
    """
    try:
        conn = snowflake.connector.connect(
            user=config['Snowflake']['user'],
            password=config['Snowflake']['password'],
            account=config['Snowflake']['account'],
            warehouse=config['Snowflake']['warehouse'],
            database=config['Snowflake']['database'],
            schema=config['Snowflake']['schema']
        )
        logging.info("Snowflake connection established successfully.")
        return conn
    except Exception as e:
        logging.error(f"Failed to connect to Snowflake: {e}")
        raise

def load_data_from_file(file_path):
    """
    Load data from a local file into a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Failed to load data from {file_path}: {e}")
        raise

def upload_data_to_snowflake(conn, data, table_name):
    """
    Upload data from a DataFrame to a Snowflake table.
    """
    try:
        write_pandas(conn, data, table_name)
        logging.info(f"Data uploaded successfully to Snowflake table {table_name}")
    except Exception as e:
        logging.error(f"Failed to upload data to Snowflake table {table_name}: {e}")
        raise

if __name__ == "__main__":
    # Load configuration
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Establish Snowflake connection
    conn = create_snowflake_connection(config)

    # Load data from local file
    file_path = config['Local']['file_path']
    data = load_data_from_file(file_path)

    # Upload data to Snowflake
    table_name = config['Snowflake']['table_name']
    upload_data_to_snowflake(conn, data, table_name)

    # Close the connection
    conn.close()