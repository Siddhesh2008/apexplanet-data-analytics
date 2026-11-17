"""
PostgreSQL Database Connection and Query Utilities
ApexPlanet Data Analytics Internship — Task 2
Author: Siddhesh (B.Tech AI & Data Science)
"""

import os
import pandas as pd
from sqlalchemy import create_engine, text

# Database connection credentials (configurable via env vars with defaults)
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "Siddhesh")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "apexplanet_analytics")

# Create SQLAlchemy Engine
CONNECTION_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(CONNECTION_URI)

def get_engine():
    """Return the active SQLAlchemy engine instance."""
    return engine

def test_connection():
    """Verify database connectivity."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();")).fetchone()
            print(f"Connected to PostgreSQL successfully:\n{result[0]}")
            return True
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False

def run_query(query: str, params: dict = None) -> pd.DataFrame:
    """
    Execute an SQL query and return the results as a Pandas DataFrame.
    
    Args:
        query: SQL query string.
        params: Optional dictionary of query parameters.
    
    Returns:
        pd.DataFrame containing the query results.
    """
    with engine.connect() as conn:
        return pd.read_sql(text(query) if params else query, conn, params=params)

def ingest_csv_to_postgres(csv_path: str = None, table_name: str = "ecommerce_transactions", if_exists: str = "replace"):
    """
    Ingest the e-commerce transactions CSV dataset into PostgreSQL.
    """
    if csv_path is None:
        candidate_paths = [
            "data/ecommerce_transactions.csv",
            "../data/ecommerce_transactions.csv",
            "ecommerce_transactions.csv",
            "../../data/ecommerce_transactions.csv"
        ]
        csv_path = next((p for p in candidate_paths if os.path.exists(p)), None)
        if not csv_path:
            raise FileNotFoundError("Could not locate ecommerce_transactions.csv")
    
    print(f"Reading dataset from: {csv_path}")
    df = pd.read_csv(csv_path)
    
    # Clean column names to lowercase snake_case for PostgreSQL standard
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    
    print(f"Ingesting {len(df):,} records into table '{table_name}'...")
    df.to_sql(table_name, engine, if_exists=if_exists, index=False, chunksize=5000)
    print(f"Successfully loaded {len(df):,} rows into '{table_name}'.")

if __name__ == "__main__":
    test_connection()
