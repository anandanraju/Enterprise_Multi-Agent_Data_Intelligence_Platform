import pyodbc


CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=ANANDAN_RAJU\\SQLEXPRESS;"
    "DATABASE=EnterpriseAnalytics;"
    "Trusted_Connection=yes;"
)


def create_schema():

    connection = pyodbc.connect(CONNECTION_STRING)
    connection.autocommit = True
    cursor = connection.cursor()

    print("Connected to EnterpriseAnalytics")

    # =========================================================
    # DROP EXISTING TABLES
    # =========================================================

    drop_tables = [
        "Transactions",
        "Support_Tickets",
        "Sales",
        "Orders",
        "Employees",
        "Products",
        "Customers",
        "Regions",
    ]

    print("\nRemoving existing tables...")

    for table in drop_tables:
        cursor.execute(
            f"""
            IF OBJECT_ID('dbo.{table}', 'U') IS NOT NULL
                DROP TABLE dbo.{table}
            """
        )
        print(f"  Removed: {table}")

    # =========================================================
    # REGIONS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Regions (
        region_id VARCHAR(20) NOT NULL PRIMARY KEY,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        sales_territory VARCHAR(100) NOT NULL,
        regional_manager VARCHAR(150) NOT NULL
    )
    """)

    # =========================================================
    # CUSTOMERS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Customers (
        customer_id VARCHAR(30) NOT NULL PRIMARY KEY,
        customer_name VARCHAR(150) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL,
        industry VARCHAR(100) NOT NULL,
        customer_segment VARCHAR(50) NOT NULL,
        account_status VARCHAR(50) NOT NULL,
        onboarding_date DATE NOT NULL
    )
    """)

    # =========================================================
    # PRODUCTS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Products (
        product_id VARCHAR(30) NOT NULL PRIMARY KEY,
        product_name VARCHAR(150) NOT NULL,
        category VARCHAR(100) NOT NULL,
        sub_category VARCHAR(100) NOT NULL,
        unit_price DECIMAL(18, 2) NOT NULL,
        standard_cost_rate DECIMAL(8, 4) NOT NULL,
        product_status VARCHAR(50) NOT NULL
    )
    """)

    # =========================================================
    # EMPLOYEES
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Employees (
        employee_id VARCHAR(30) NOT NULL PRIMARY KEY,
        employee_name VARCHAR(150) NOT NULL,
        department VARCHAR(100) NOT NULL,
        role VARCHAR(100) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        joining_date DATE NOT NULL,
        employment_status VARCHAR(50) NOT NULL
    )
    """)

    # =========================================================
    # ORDERS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Orders (
        order_id VARCHAR(30) NOT NULL PRIMARY KEY,
        customer_id VARCHAR(30) NOT NULL,
        product_id VARCHAR(30) NOT NULL,
        order_date DATE NOT NULL,
        quantity INT NOT NULL,
        discount DECIMAL(8, 4) NOT NULL,
        revenue DECIMAL(18, 2) NOT NULL,
        cost DECIMAL(18, 2) NOT NULL,
        profit DECIMAL(18, 2) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        sales_channel VARCHAR(50) NOT NULL,
        order_status VARCHAR(50) NOT NULL,

        CONSTRAINT FK_Orders_Customers
            FOREIGN KEY (customer_id)
            REFERENCES dbo.Customers(customer_id),

        CONSTRAINT FK_Orders_Products
            FOREIGN KEY (product_id)
            REFERENCES dbo.Products(product_id)
    )
    """)

    # =========================================================
    # SALES
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Sales (
        sales_id VARCHAR(30) NOT NULL PRIMARY KEY,
        order_id VARCHAR(30) NOT NULL,
        order_date DATE NOT NULL,
        customer_id VARCHAR(30) NOT NULL,
        product_id VARCHAR(30) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        sales_channel VARCHAR(50) NOT NULL,
        quantity INT NOT NULL,
        discount DECIMAL(8, 4) NOT NULL,
        revenue DECIMAL(18, 2) NOT NULL,
        cost DECIMAL(18, 2) NOT NULL,
        profit DECIMAL(18, 2) NOT NULL,
        payment_status VARCHAR(50) NOT NULL,

        CONSTRAINT FK_Sales_Orders
            FOREIGN KEY (order_id)
            REFERENCES dbo.Orders(order_id),

        CONSTRAINT FK_Sales_Customers
            FOREIGN KEY (customer_id)
            REFERENCES dbo.Customers(customer_id),

        CONSTRAINT FK_Sales_Products
            FOREIGN KEY (product_id)
            REFERENCES dbo.Products(product_id)
    )
    """)

    # =========================================================
    # SUPPORT TICKETS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Support_Tickets (
        ticket_id VARCHAR(30) NOT NULL PRIMARY KEY,
        customer_id VARCHAR(30) NOT NULL,
        customer_name VARCHAR(150) NOT NULL,
        issue_type VARCHAR(100) NOT NULL,
        priority VARCHAR(50) NOT NULL,
        created_date DATE NOT NULL,
        resolution_time_hours DECIMAL(10, 2) NULL,
        status VARCHAR(50) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,
        assigned_team VARCHAR(100) NOT NULL,

        CONSTRAINT FK_SupportTickets_Customers
            FOREIGN KEY (customer_id)
            REFERENCES dbo.Customers(customer_id)
    )
    """)

    # =========================================================
    # TRANSACTIONS
    # =========================================================

    cursor.execute("""
    CREATE TABLE dbo.Transactions (
        transaction_id VARCHAR(30) NOT NULL PRIMARY KEY,
        sales_id VARCHAR(30) NOT NULL,
        customer_id VARCHAR(30) NOT NULL,
        transaction_date DATE NOT NULL,
        transaction_type VARCHAR(50) NOT NULL,
        amount DECIMAL(18, 2) NOT NULL,
        currency VARCHAR(10) NOT NULL,
        payment_status VARCHAR(50) NOT NULL,
        payment_method VARCHAR(50) NOT NULL,
        region VARCHAR(100) NOT NULL,
        city VARCHAR(100) NOT NULL,

        CONSTRAINT FK_Transactions_Sales
            FOREIGN KEY (sales_id)
            REFERENCES dbo.Sales(sales_id),

        CONSTRAINT FK_Transactions_Customers
            FOREIGN KEY (customer_id)
            REFERENCES dbo.Customers(customer_id)
    )
    """)

    print("\nDatabase schema recreated successfully")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_schema()