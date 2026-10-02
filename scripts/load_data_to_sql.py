from pathlib import Path

import pandas as pd
import pyodbc


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(r"D:\Data Science\Projects\Ai_Creation\Enterprise_Multi-Agent_Data_Intelligence_Platform")
RAW_DIR = PROJECT_ROOT / "data" / "raw"


# ---------------------------------------------------------
# SQL Server connection
# ---------------------------------------------------------

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ANANDAN_RAJU\\SQLEXPRESS;"
    "DATABASE=EnterpriseAnalytics;"
    "Trusted_Connection=yes;"
)


# ---------------------------------------------------------
# Load configuration
# ---------------------------------------------------------

TABLES = [
    "Regions",
    "Customers",
    "Products",
    "Employees",
    "Orders",
    "Sales",
    "Support_Tickets",
    "Transactions",
]


def get_connection():
    return pyodbc.connect(CONNECTION_STRING)


def clear_tables(cursor):
    """
    Delete existing records in reverse foreign-key order.
    This allows the script to be safely re-run.
    """

    delete_order = [
        "Transactions",
        "Support_Tickets",
        "Sales",
        "Orders",
        "Employees",
        "Products",
        "Customers",
        "Regions",
    ]

    print("\nClearing existing table data...")

    for table in delete_order:
        cursor.execute(f"DELETE FROM dbo.{table}")
        print(f"  Cleared: {table}")

def load_table(connection, table_name):
    csv_path = RAW_DIR / f"{table_name}.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(csv_path)

    if df.empty:
        print(f"  Warning: {table_name}.csv is empty")
        return 0

    # Convert date columns to Python date objects
    date_columns = [
        "onboarding_date",
        "joining_date",
        "order_date",
        "created_date",
        "transaction_date",
    ]

    for column in date_columns:
        if column in df.columns:
            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            ).dt.date

    # Convert numeric columns explicitly
    numeric_columns = [
        "quantity",
        "discount",
        "revenue",
        "cost",
        "profit",
        "unit_price",
        "standard_cost_rate",
        "resolution_time_hours",
        "amount",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # Convert every value to a Python-native value.
    # This is important for pyodbc, especially NaN -> None.
    rows = []

    for row in df.itertuples(index=False, name=None):
        cleaned_row = []

        for value in row:
            if pd.isna(value):
                cleaned_row.append(None)
            elif hasattr(value, "item"):
                cleaned_row.append(value.item())
            else:
                cleaned_row.append(value)

        rows.append(tuple(cleaned_row))

    columns = list(df.columns)

    column_names = ", ".join(
        f"[{column}]" for column in columns
    )

    placeholders = ", ".join(
        "?" for _ in columns
    )

    sql = f"""
        INSERT INTO dbo.{table_name}
        ({column_names})
        VALUES ({placeholders})
    """

    cursor = connection.cursor()
    cursor.fast_executemany = True

    try:
        cursor.executemany(sql, rows)
        connection.commit()
    finally:
        cursor.close()

    print(f"  Inserted: {len(rows):,} rows")

    return len(rows)

def verify_counts(connection):
    """
    Verify row counts after loading.
    """

    print("\n" + "=" * 70)
    print("SQL SERVER ROW COUNT VERIFICATION")
    print("=" * 70)

    cursor = connection.cursor()

    for table in TABLES:
        cursor.execute(
            f"SELECT COUNT(*) FROM dbo.{table}"
        )

        count = cursor.fetchone()[0]

        print(f"{table:<20} {count:>10,}")

    cursor.close()


def main():

    print("=" * 70)
    print("LOADING ENTERPRISE DATA INTO SQL SERVER")
    print("=" * 70)

    print(f"\nProject root:")
    print(PROJECT_ROOT)

    print(f"\nCSV directory:")
    print(RAW_DIR)

    # Check CSV directory.
    if not RAW_DIR.exists():
        raise FileNotFoundError(
            f"Data directory not found: {RAW_DIR}"
        )

    print("\nConnecting to SQL Server...")

    connection = get_connection()

    print("SQL Server connection successful")
    print("Database: EnterpriseAnalytics")

    try:

        cursor = connection.cursor()

        # Clear old data so the script can be safely re-run.
        clear_tables(cursor)

        cursor.close()

        total_rows = 0

        for table in TABLES:
            total_rows += load_table(
                connection,
                table
            )

        verify_counts(connection)

        print("\n" + "=" * 70)
        print("DATA LOAD COMPLETED SUCCESSFULLY")
        print("=" * 70)

        print(f"\nTotal rows loaded: {total_rows:,}")

    except Exception:
        connection.rollback()
        print("\nData loading failed.")
        raise

    finally:
        connection.close()


if __name__ == "__main__":
    main()