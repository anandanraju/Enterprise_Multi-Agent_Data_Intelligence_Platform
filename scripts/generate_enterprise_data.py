from pathlib import Path
from datetime import date, timedelta
import random

import numpy as np
import pandas as pd
from faker import Faker


## CONFIGURATION


SEED = 42

random.seed(SEED)
np.random.seed(SEED)

fake = Faker()
Faker.seed(SEED)

## Automatically detect project root.
## Project structure:
## Enterprise_Multi-Agent_Data_Intelligence/
## ├── scripts/
## ├── data/
## │   └── raw/
## └── ...

PROJECT_ROOT = Path(r"D:\Data Science\Projects\Ai_Creation\Enterprise_Multi-Agent_Data_Intelligence_Platform")
RAW_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

START_DATE = date(2024, 1, 1)
END_DATE = date(2026, 9, 30)

## DATASET SIZE

CUSTOMER_COUNT = 1000
PRODUCT_COUNT = 100
EMPLOYEE_COUNT = 500
ORDER_COUNT = 50000
SUPPORT_TICKET_COUNT = 10000

## REFERENCE DATA

REGIONS_CITIES = {
    "South": [
        "Chennai",
        "Bengaluru",
        "Hyderabad",
        "Coimbatore",
        "Kochi",
    ],
    "West": [
        "Mumbai",
        "Pune",
        "Ahmedabad",
        "Surat",
    ],
    "North": [
        "Delhi",
        "Jaipur",
        "Lucknow",
        "Chandigarh",
    ],
    "East": [
        "Kolkata",
        "Bhubaneswar",
        "Patna",
        "Guwahati",
    ],
    "Central": [
        "Bhopal",
        "Indore",
        "Nagpur",
        "Raipur",
    ],
    "International": [
        "London",
        "New York",
        "Singapore",
        "Dubai",
    ],
}

COUNTRY_BY_CITY = {
    "Chennai": "India",
    "Bengaluru": "India",
    "Hyderabad": "India",
    "Coimbatore": "India",
    "Kochi": "India",
    "Mumbai": "India",
    "Pune": "India",
    "Ahmedabad": "India",
    "Surat": "India",
    "Delhi": "India",
    "Jaipur": "India",
    "Lucknow": "India",
    "Chandigarh": "India",
    "Kolkata": "India",
    "Bhubaneswar": "India",
    "Patna": "India",
    "Guwahati": "India",
    "Bhopal": "India",
    "Indore": "India",
    "Nagpur": "India",
    "Raipur": "India",
    "London": "UK",
    "New York": "USA",
    "Singapore": "Singapore",
    "Dubai": "UAE",
}

INDUSTRIES = [
    "Manufacturing",
    "Retail",
    "Healthcare",
    "Technology",
    "Automotive",
    "Finance",
    "Logistics",
    "Energy",
    "Telecommunications",
    "Professional Services",
]

CUSTOMER_SEGMENTS = [
    "Enterprise",
    "Mid-Market",
    "SMB",
]

CUSTOMER_SEGMENT_WEIGHTS = [0.20, 0.35, 0.45]

ACCOUNT_STATUSES = [
    "Active",
    "At Risk",
    "Inactive",
]

ACCOUNT_STATUS_WEIGHTS = [0.82, 0.12, 0.06]

PRODUCT_CATEGORIES = {
    "Hardware": [
        "Server",
        "Laptop",
        "Network Device",
        "Storage Unit",
        "Monitor",
        "Industrial Sensor",
    ],
    "Software": [
        "Analytics License",
        "Security Suite",
        "ERP Module",
        "CRM License",
        "Data Platform",
        "Workflow Platform",
    ],
    "Services": [
        "Implementation",
        "Consulting",
        "Support Plan",
        "Training",
        "Managed Service",
    ],
    "Cloud": [
        "Compute Package",
        "Storage Package",
        "AI Platform",
        "Backup Service",
        "Cloud Database",
    ],
}

PRODUCT_STATUSES = [
    "Active",
    "Discontinued",
]

PRODUCT_STATUS_WEIGHTS = [0.92, 0.08]

DEPARTMENTS = [
    "Sales",
    "Operations",
    "Finance",
    "Customer Success",
    "IT",
    "Analytics",
    "Support",
    "Marketing",
    "Procurement",
    "Human Resources",
]

ROLES = {
    "Sales": [
        "Account Executive",
        "Sales Manager",
        "Sales Analyst",
        "Sales Executive",
    ],
    "Operations": [
        "Operations Executive",
        "Operations Manager",
        "Process Analyst",
        "Operations Analyst",
    ],
    "Finance": [
        "Financial Analyst",
        "Finance Manager",
        "Billing Specialist",
        "Financial Controller",
    ],
    "Customer Success": [
        "Customer Success Manager",
        "Account Specialist",
        "Customer Success Analyst",
    ],
    "IT": [
        "Systems Engineer",
        "Application Support Engineer",
        "IT Manager",
        "Cloud Engineer",
    ],
    "Analytics": [
        "BI Analyst",
        "Data Analyst",
        "Analytics Engineer",
        "Senior Data Analyst",
    ],
    "Support": [
        "Support Specialist",
        "Support Lead",
        "Technical Support Engineer",
    ],
    "Marketing": [
        "Marketing Analyst",
        "Marketing Manager",
        "Campaign Specialist",
    ],
    "Procurement": [
        "Procurement Analyst",
        "Procurement Manager",
        "Purchasing Specialist",
    ],
    "Human Resources": [
        "HR Analyst",
        "HR Manager",
        "HR Executive",
    ],
}

EMPLOYMENT_STATUSES = [
    "Active",
    "On Leave",
    "Exited",
]

EMPLOYMENT_STATUS_WEIGHTS = [0.90, 0.04, 0.06]

SALES_CHANNELS = [
    "Direct",
    "Partner",
    "Online",
]

ORDER_STATUSES = [
    "Completed",
    "Pending",
    "Cancelled",
]

ORDER_STATUS_WEIGHTS = [0.90, 0.07, 0.03]

PAYMENT_STATUSES = [
    "Paid",
    "Pending",
    "Overdue",
]

PAYMENT_STATUS_WEIGHTS = [0.86, 0.09, 0.05]

PAYMENT_METHODS = [
    "Bank Transfer",
    "Credit Card",
    "UPI",
    "Invoice",
]

TICKET_TYPES = [
    "Billing Issue",
    "Product Defect",
    "Access Request",
    "Performance",
    "Integration",
    "How-to Query",
    "Data Quality",
]

TICKET_PRIORITIES = [
    "Critical",
    "High",
    "Medium",
    "Low",
]

TICKET_PRIORITY_WEIGHTS = [0.04, 0.16, 0.52, 0.28]

TICKET_STATUSES = [
    "Resolved",
    "In Progress",
    "Open",
    "Escalated",
]

TICKET_STATUS_WEIGHTS = [0.72, 0.13, 0.10, 0.05]



## HELPER FUNCTIONS


def random_date(start_date: date, end_date: date) -> date:
    """Generate a random date between two dates."""

    days = (end_date - start_date).days

    return start_date + timedelta(
        days=random.randint(0, days)
    )


def save_dataset(df: pd.DataFrame, filename: str) -> None:
    """Save both CSV and Excel versions."""

    csv_path = RAW_DIR / f"{filename}.csv"
    excel_path = RAW_DIR / f"{filename}.xlsx"

    df.to_csv(
        csv_path,
        index=False,
        date_format="%Y-%m-%d",
    )

    with pd.ExcelWriter(
        excel_path,
        engine="openpyxl",
        date_format="yyyy-mm-dd",
        datetime_format="yyyy-mm-dd",
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Data",
        )

        worksheet = writer.sheets["Data"]

        worksheet.freeze_panes = "A2"

        worksheet.auto_filter.ref = worksheet.dimensions

        for column_cells in worksheet.columns:

            max_length = 0

            for cell in column_cells[:200]:

                if cell.value is not None:
                    max_length = max(
                        max_length,
                        len(str(cell.value)),
                    )

            width = min(
                max(max_length + 2, 12),
                32,
            )

            worksheet.column_dimensions[
                column_cells[0].column_letter
            ].width = width

    print(
        f"Created: {filename:<20} "
        f"Rows: {len(df):>7,} "
        f"Columns: {len(df.columns):>2}"
    )



## REGIONS


def generate_regions() -> pd.DataFrame:

    rows = []

    region_number = 1

    for region, cities in REGIONS_CITIES.items():

        for city in cities:

            rows.append({
                "region_id": f"REG-{region_number:03d}",
                "region": region,
                "city": city,
                "country": COUNTRY_BY_CITY[city],
                "sales_territory": f"{region} Territory",
                "regional_manager": fake.name(),
            })

            region_number += 1

    return pd.DataFrame(rows)



## CUSTOMERS


def generate_customers() -> pd.DataFrame:

    rows = []

    all_cities = [
        city
        for cities in REGIONS_CITIES.values()
        for city in cities
    ]

    city_region = {
        city: region
        for region, cities in REGIONS_CITIES.items()
        for city in cities
    }

    for i in range(1, CUSTOMER_COUNT + 1):

        city = random.choice(all_cities)
        region = city_region[city]

        rows.append({
            "customer_id": f"CUST-{i:05d}",
            "customer_name": fake.company(),
            "region": region,
            "city": city,
            "country": COUNTRY_BY_CITY[city],
            "industry": random.choice(INDUSTRIES),
            "customer_segment": random.choices(
                CUSTOMER_SEGMENTS,
                weights=CUSTOMER_SEGMENT_WEIGHTS,
                k=1,
            )[0],
            "account_status": random.choices(
                ACCOUNT_STATUSES,
                weights=ACCOUNT_STATUS_WEIGHTS,
                k=1,
            )[0],
            "onboarding_date": random_date(
                date(2020, 1, 1),
                date(2025, 12, 31),
            ),
        })

    return pd.DataFrame(rows)



## PRODUCTS


def generate_products() -> pd.DataFrame:

    rows = []

    product_templates = []

    for category, sub_categories in PRODUCT_CATEGORIES.items():

        for sub_category in sub_categories:

            product_templates.append(
                (category, sub_category)
            )

    for i in range(1, PRODUCT_COUNT + 1):

        category, sub_category = random.choice(
            product_templates
        )

        unit_price = round(
            random.uniform(5000, 250000),
            2,
        )

        standard_cost_rate = round(
            random.uniform(0.45, 0.78),
            2,
        )

        rows.append({
            "product_id": f"PROD-{i:04d}",
            "product_name": (
                f"{sub_category} "
                f"{random.choice(['Standard', 'Pro', 'Advanced', 'Enterprise'])} "
                f"{i:02d}"
            ),
            "category": category,
            "sub_category": sub_category,
            "unit_price": unit_price,
            "standard_cost_rate": standard_cost_rate,
            "product_status": random.choices(
                PRODUCT_STATUSES,
                weights=PRODUCT_STATUS_WEIGHTS,
                k=1,
            )[0],
        })

    return pd.DataFrame(rows)



## EMPLOYEES


def generate_employees() -> pd.DataFrame:

    rows = []

    all_cities = [
        city
        for cities in REGIONS_CITIES.values()
        for city in cities
    ]

    city_region = {
        city: region
        for region, cities in REGIONS_CITIES.items()
        for city in cities
    }

    for i in range(1, EMPLOYEE_COUNT + 1):

        department = random.choice(DEPARTMENTS)
        city = random.choice(all_cities)

        rows.append({
            "employee_id": f"EMP-{i:05d}",
            "employee_name": fake.name(),
            "department": department,
            "role": random.choice(
                ROLES[department]
            ),
            "region": city_region[city],
            "city": city,
            "joining_date": random_date(
                date(2018, 1, 1),
                date(2025, 12, 31),
            ),
            "employment_status": random.choices(
                EMPLOYMENT_STATUSES,
                weights=EMPLOYMENT_STATUS_WEIGHTS,
                k=1,
            )[0],
        })

    return pd.DataFrame(rows)



## ORDERS


def generate_orders(
    customers: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:

    rows = []

    customer_ids = customers["customer_id"].tolist()
    product_ids = products["product_id"].tolist()

    customer_lookup = (
        customers
        .set_index("customer_id")
        .to_dict("index")
    )

    product_lookup = (
        products
        .set_index("product_id")
        .to_dict("index")
    )

    for i in range(1, ORDER_COUNT + 1):

        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)

        customer = customer_lookup[customer_id]
        product = product_lookup[product_id]

        order_date = random_date(
            START_DATE,
            END_DATE,
        )

        quantity = random.randint(1, 20)

        discount = random.choice([
            0.00,
            0.02,
            0.05,
            0.08,
            0.10,
            0.15,
        ])

        unit_price = product["unit_price"]
        cost_rate = product["standard_cost_rate"]

        revenue = round(
            quantity
            * unit_price
            * (1 - discount),
            2,
        )

        cost = round(
            quantity
            * unit_price
            * cost_rate,
            2,
        )

        profit = round(
            revenue - cost,
            2,
        )

        rows.append({
            "order_id": f"ORD-{i:07d}",
            "customer_id": customer_id,
            "product_id": product_id,
            "order_date": order_date,
            "quantity": quantity,
            "discount": discount,
            "revenue": revenue,
            "cost": cost,
            "profit": profit,
            "region": customer["region"],
            "city": customer["city"],
            "sales_channel": random.choice(
                SALES_CHANNELS
            ),
            "order_status": random.choices(
                ORDER_STATUSES,
                weights=ORDER_STATUS_WEIGHTS,
                k=1,
            )[0],
        })

    return pd.DataFrame(rows)



## BUSINESS SCENARIO 1
## CHENNAI Q2 2026 REVENUE DECLINE


def inject_chennai_q2_decline(
    orders: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:

    orders = orders.copy()

    product_lookup = (
        products
        .set_index("product_id")
        .to_dict("index")
    )

    chennai_q2_mask = (
        (orders["city"] == "Chennai")
        & (orders["order_date"] >= date(2026, 4, 1))
        & (orders["order_date"] <= date(2026, 6, 30))
        & (orders["order_status"] == "Completed")
    )

    affected_indices = orders[
        chennai_q2_mask
    ].sample(
        frac=0.65,
        random_state=SEED,
    ).index

    for idx in affected_indices:

        old_quantity = int(
            orders.loc[idx, "quantity"]
        )

        new_quantity = max(
            1,
            int(old_quantity * 0.55),
        )

        orders.loc[idx, "quantity"] = new_quantity

        product_id = orders.loc[
            idx,
            "product_id"
        ]

        product = product_lookup[product_id]

        unit_price = float(
            product["unit_price"]
        )

        cost_rate = float(
            product["standard_cost_rate"]
        )

        discount = float(
            orders.loc[idx, "discount"]
        )

        revenue = round(
            new_quantity
            * unit_price
            * (1 - discount),
            2,
        )

        cost = round(
            new_quantity
            * unit_price
            * cost_rate,
            2,
        )

        orders.loc[idx, "revenue"] = revenue
        orders.loc[idx, "cost"] = cost
        orders.loc[idx, "profit"] = round(
            revenue - cost,
            2,
        )

    return orders



## SALES


def generate_sales(
    orders: pd.DataFrame,
) -> pd.DataFrame:

    sales = orders[
        orders["order_status"] == "Completed"
    ].copy()

    sales = sales[
        [
            "order_id",
            "order_date",
            "customer_id",
            "product_id",
            "region",
            "city",
            "sales_channel",
            "quantity",
            "discount",
            "revenue",
            "cost",
            "profit",
        ]
    ].reset_index(drop=True)

    sales.insert(
        0,
        "sales_id",
        [
            f"SALE-{i:07d}"
            for i in range(1, len(sales) + 1)
        ],
    )

    sales["payment_status"] = [
        random.choices(
            PAYMENT_STATUSES,
            weights=PAYMENT_STATUS_WEIGHTS,
            k=1,
        )[0]
        for _ in range(len(sales))
    ]

    return sales



## SUPPORT TICKETS


def generate_support_tickets(
    customers: pd.DataFrame,
) -> pd.DataFrame:

    rows = []

    customer_ids = customers["customer_id"].tolist()

    customer_lookup = (
        customers
        .set_index("customer_id")
        .to_dict("index")
    )

    for i in range(
        1,
        SUPPORT_TICKET_COUNT + 1,
    ):

        customer_id = random.choice(
            customer_ids
        )

        customer = customer_lookup[
            customer_id
        ]

        status = random.choices(
            TICKET_STATUSES,
            weights=TICKET_STATUS_WEIGHTS,
            k=1,
        )[0]

        priority = random.choices(
            TICKET_PRIORITIES,
            weights=TICKET_PRIORITY_WEIGHTS,
            k=1,
        )[0]

        if status == "Resolved":

            if priority == "Critical":
                resolution_time = random.randint(
                    1,
                    12,
                )

            elif priority == "High":
                resolution_time = random.randint(
                    4,
                    24,
                )

            elif priority == "Medium":
                resolution_time = random.randint(
                    8,
                    48,
                )

            else:
                resolution_time = random.randint(
                    12,
                    96,
                )

        else:
            resolution_time = None

        rows.append({
            "ticket_id": f"TKT-{i:07d}",
            "customer_id": customer_id,
            "customer_name": customer["customer_name"],
            "issue_type": random.choice(
                TICKET_TYPES
            ),
            "priority": priority,
            "created_date": random_date(
                START_DATE,
                END_DATE,
            ),
            "resolution_time_hours": resolution_time,
            "status": status,
            "region": customer["region"],
            "city": customer["city"],
            "assigned_team": random.choice([
                "Support L1",
                "Support L2",
                "Billing Team",
                "Product Team",
                "Data Team",
            ]),
        })

    return pd.DataFrame(rows)



## TRANSACTIONS


def generate_transactions(
    sales: pd.DataFrame,
) -> pd.DataFrame:

    rows = []

    for i, row in sales.iterrows():

        rows.append({
            "transaction_id": (
                f"TXN-{i + 1:07d}"
            ),
            "sales_id": row["sales_id"],
            "customer_id": row["customer_id"],
            "transaction_date": row["order_date"],
            "transaction_type": "Sale",
            "amount": row["revenue"],
            "currency": "INR",
            "payment_status": row["payment_status"],
            "payment_method": random.choice(
                PAYMENT_METHODS
            ),
            "region": row["region"],
            "city": row["city"],
        })

    return pd.DataFrame(rows)



## DATA VALIDATION


def validate_data(
    regions: pd.DataFrame,
    customers: pd.DataFrame,
    products: pd.DataFrame,
    employees: pd.DataFrame,
    orders: pd.DataFrame,
    sales: pd.DataFrame,
    tickets: pd.DataFrame,
    transactions: pd.DataFrame,
) -> None:

    print("\n")
    print("=" * 70)
    print("DATA VALIDATION")
    print("=" * 70)

    datasets = {
        "Regions": regions,
        "Customers": customers,
        "Products": products,
        "Employees": employees,
        "Orders": orders,
        "Sales": sales,
        "Support Tickets": tickets,
        "Transactions": transactions,
    }

    for name, df in datasets.items():

        print(f"\n{name}")

        print(
            f"  Rows       : {len(df):,}"
        )

        print(
            f"  Columns    : {len(df.columns)}"
        )

        print(
            f"  Duplicate rows : "
            f"{df.duplicated().sum():,}"
        )

        print(
            f"  Null cells    : "
            f"{df.isna().sum().sum():,}"
        )

    ## --------------------------------------------------------
    ## CUSTOMER FOREIGN KEY
    ## --------------------------------------------------------

    customer_ids = set(
        customers["customer_id"]
    )

    invalid_orders = (
        ~orders["customer_id"].isin(
            customer_ids
        )
    )

    invalid_tickets = (
        ~tickets["customer_id"].isin(
            customer_ids
        )
    )

    invalid_transactions = (
        ~transactions["customer_id"].isin(
            customer_ids
        )
    )

    print("\nForeign-key validation")

    print(
        f"  Invalid order customers       : "
        f"{invalid_orders.sum()}"
    )

    print(
        f"  Invalid ticket customers      : "
        f"{invalid_tickets.sum()}"
    )

    print(
        f"  Invalid transaction customers : "
        f"{invalid_transactions.sum()}"
    )

    ## --------------------------------------------------------
    ## PRODUCT FOREIGN KEY
    ## --------------------------------------------------------

    product_ids = set(
        products["product_id"]
    )

    invalid_order_products = (
        ~orders["product_id"].isin(
            product_ids
        )
    )

    print(
        f"  Invalid order products        : "
        f"{invalid_order_products.sum()}"
    )

    ## --------------------------------------------------------
    ## SALES -> ORDERS
    ## --------------------------------------------------------

    order_ids = set(
        orders["order_id"]
    )

    invalid_sales_orders = (
        ~sales["order_id"].isin(
            order_ids
        )
    )

    print(
        f"  Invalid sales orders          : "
        f"{invalid_sales_orders.sum()}"
    )

    ## --------------------------------------------------------
    ## TRANSACTIONS -> SALES
    ## --------------------------------------------------------

    sales_ids = set(
        sales["sales_id"]
    )

    invalid_transaction_sales = (
        ~transactions["sales_id"].isin(
            sales_ids
        )
    )

    print(
        f"  Invalid transaction sales     : "
        f"{invalid_transaction_sales.sum()}"
    )

    ## --------------------------------------------------------
    ## BUSINESS CALCULATIONS
    ## --------------------------------------------------------

    expected_profit = (
        orders["revenue"]
        - orders["cost"]
    ).round(2)

    profit_mismatch = (
        expected_profit
        != orders["profit"].round(2)
    )

    print(
        f"\nProfit calculation mismatches : "
        f"{profit_mismatch.sum()}"
    )

    ## --------------------------------------------------------
    ## NEGATIVE VALUES
    ## --------------------------------------------------------

    negative_revenue = (
        orders["revenue"] < 0
    ).sum()

    negative_quantity = (
        orders["quantity"] <= 0
    ).sum()

    print(
        f"Negative revenue values        : "
        f"{negative_revenue}"
    )

    print(
        f"Invalid quantity values         : "
        f"{negative_quantity}"
    )

    ## --------------------------------------------------------
    ## DATE RANGE
    ## --------------------------------------------------------

    print(
        f"\nOrder date range               : "
        f"{orders['order_date'].min()} "
        f"to "
        f"{orders['order_date'].max()}"
    )

    ## --------------------------------------------------------
    ## CHENNAI Q2 DEMO CHECK
    ## --------------------------------------------------------

    chennai_q1 = orders[
        (orders["city"] == "Chennai")
        & (
            orders["order_date"]
            >= date(2026, 1, 1)
        )
        & (
            orders["order_date"]
            <= date(2026, 3, 31)
        )
        & (
            orders["order_status"]
            == "Completed"
        )
    ]["revenue"].sum()

    chennai_q2 = orders[
        (orders["city"] == "Chennai")
        & (
            orders["order_date"]
            >= date(2026, 4, 1)
        )
        & (
            orders["order_date"]
            <= date(2026, 6, 30)
        )
        & (
            orders["order_status"]
            == "Completed"
        )
    ]["revenue"].sum()

    if chennai_q1 > 0:

        change_pct = (
            (chennai_q2 - chennai_q1)
            / chennai_q1
        ) * 100

    else:
        change_pct = 0

    print("\nDemo scenario check")
    print(
        f"  Chennai Q1 2026 revenue : "
        f"₹{chennai_q1:,.2f}"
    )
    print(
        f"  Chennai Q2 2026 revenue : "
        f"₹{chennai_q2:,.2f}"
    )
    print(
        f"  Q2 change                : "
        f"{change_pct:.2f}%"
    )

    print("\nValidation completed.")



## DATASET README


def create_readme() -> None:

    readme_content = """
## Enterprise Multi-Agent Data Intelligence & Decision Support Platform

#### Dataset

This directory contains synthetic enterprise data created for
development, testing, analytics, Text-to-SQL, RAG, multi-agent
workflows and visualization.

No real customers, employees or financial transactions are represented.

#### Files

- Customers.csv / Customers.xlsx
- Products.csv / Products.xlsx
- Orders.csv / Orders.xlsx
- Sales.csv / Sales.xlsx
- Employees.csv / Employees.xlsx
- Support_Tickets.csv / Support_Tickets.xlsx
- Regions.csv / Regions.xlsx
- Transactions.csv / Transactions.xlsx

#### Relationships

Customers
    |
    +---- Orders
    |       |
    |       +---- Products
    |
    +---- Support_Tickets
    |
    +---- Transactions

Orders
    |
    +---- Sales
            |
            +---- Transactions

#### Primary Keys

Regions
    region_id

Customers
    customer_id

Products
    product_id

Employees
    employee_id

Orders
    order_id

Sales
    sales_id

Support_Tickets
    ticket_id

Transactions
    transaction_id

#### Important Foreign Keys

Orders.customer_id
    -> Customers.customer_id

Orders.product_id
    -> Products.product_id

Sales.order_id
    -> Orders.order_id

Sales.customer_id
    -> Customers.customer_id

Transactions.sales_id
    -> Sales.sales_id

Transactions.customer_id
    -> Customers.customer_id

Support_Tickets.customer_id
    -> Customers.customer_id

#### Date Range

2024-01-01 through 2026-09-30

#### Currency

Synthetic financial values are represented in INR.

#### Business Scenario

A controlled synthetic revenue-decline scenario is introduced for
Chennai during Q2 2026.

The scenario is intentionally generated for testing the analytics
agent's ability to:

1. Compare periods.
2. Identify revenue changes.
3. Identify affected customers.
4. Identify affected products.
5. Analyze quantity changes.
6. Analyze discounts.
7. Analyze sales channels.
8. Generate supporting visualizations.
9. Produce a grounded explanation.

The scenario is synthetic and must not be interpreted as real-world
business information.

#### Reproducibility

Random seed:

42

Running the generator with the same configuration and seed produces
reproducible synthetic data.
"""

    path = RAW_DIR / "README.md"

    path.write_text(
        readme_content.strip(),
        encoding="utf-8",
    )



## DATASET SUMMARY


def create_summary(
    datasets: dict,
) -> None:

    rows = []

    for filename, df in datasets.items():

        rows.append({
            "file": filename,
            "rows": len(df),
            "columns": len(df.columns),
        })

    summary_df = pd.DataFrame(rows)

    summary_path = (
        RAW_DIR / "dataset_summary.csv"
    )

    summary_df.to_csv(
        summary_path,
        index=False,
    )

    print("\n")
    print("=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)

    print(
        summary_df.to_string(
            index=False
        )
    )



## MAIN


def main():

    print("=" * 70)
    print(
        "ENTERPRISE DATASET GENERATION"
    )
    print("=" * 70)

    print(
        f"\nProject root:\n{PROJECT_ROOT}"
    )

    print(
        f"\nOutput directory:\n{RAW_DIR}"
    )

    print(
        "\nGenerating datasets...\n"
    )

    ## --------------------------------------------------------
    ## MASTER DATA
    ## --------------------------------------------------------

    regions = generate_regions()

    save_dataset(
        regions,
        "Regions",
    )

    customers = generate_customers()

    save_dataset(
        customers,
        "Customers",
    )

    products = generate_products()

    save_dataset(
        products,
        "Products",
    )

    employees = generate_employees()

    save_dataset(
        employees,
        "Employees",
    )

    ## --------------------------------------------------------
    ## TRANSACTIONAL DATA
    ## --------------------------------------------------------

    orders = generate_orders(
        customers,
        products,
    )

    ## Inject controlled business scenario
    orders = inject_chennai_q2_decline(
        orders,
        products,
    )

    save_dataset(
        orders,
        "Orders",
    )

    sales = generate_sales(
        orders,
    )

    save_dataset(
        sales,
        "Sales",
    )

    support_tickets = (
        generate_support_tickets(
            customers
        )
    )

    save_dataset(
        support_tickets,
        "Support_Tickets",
    )

    transactions = (
        generate_transactions(
            sales
        )
    )

    save_dataset(
        transactions,
        "Transactions",
    )

    ## --------------------------------------------------------
    ## VALIDATION
    ## --------------------------------------------------------

    validate_data(
        regions=regions,
        customers=customers,
        products=products,
        employees=employees,
        orders=orders,
        sales=sales,
        tickets=support_tickets,
        transactions=transactions,
    )

    ## --------------------------------------------------------
    ## DOCUMENTATION
    ## --------------------------------------------------------

    create_readme()

    datasets = {
        "Regions": regions,
        "Customers": customers,
        "Products": products,
        "Employees": employees,
        "Orders": orders,
        "Sales": sales,
        "Support_Tickets": support_tickets,
        "Transactions": transactions,
    }

    create_summary(
        datasets
    )

    print("\n")
    print("=" * 70)
    print(
        "DATASET GENERATION COMPLETED"
    )
    print("=" * 70)

    print(
        f"\nFiles created in:\n{RAW_DIR}"
    )



## ENTRY POINT


if __name__ == "__main__":
    main()