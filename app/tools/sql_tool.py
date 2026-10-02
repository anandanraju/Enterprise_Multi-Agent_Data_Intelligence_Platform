from typing import Any

import pyodbc


CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ANANDAN_RAJU\\SQLEXPRESS;"
    "DATABASE=EnterpriseAnalytics;"
    "Trusted_Connection=yes;"
)


def get_connection():
    """Create a connection to SQL Server."""
    return pyodbc.connect(CONNECTION_STRING)


def execute_query(sql: str) -> list[dict[str, Any]]:
    """
    Execute a read-only SQL query and return the result
    as a list of dictionaries.
    """

    sql_clean = sql.strip().lower()

    if not (
        sql_clean.startswith("select")
        or sql_clean.startswith("with")
    ):
        raise ValueError(
            "Only SELECT and WITH queries are allowed."
        )

    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        columns = [column[0] for column in cursor.description]

        rows = cursor.fetchall()

        results = [
            dict(zip(columns, row))
            for row in rows
        ]

        cursor.close()

        return results

    finally:
        connection.close()


if __name__ == "__main__":

    test_sql = """
    SELECT TOP 10
        customer_id,
        customer_name,
        region,
        city,
        customer_segment
    FROM dbo.Customers
    ORDER BY customer_id;
    """

    results = execute_query(test_sql)

    print("\nSQL Query Test")
    print("=" * 60)

    for row in results:
        print(row)

    print(f"\nRows returned: {len(results)}")