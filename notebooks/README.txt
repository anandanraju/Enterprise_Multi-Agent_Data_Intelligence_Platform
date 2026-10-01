
These files contain fictional/synthetic data created for a GenAI analytics portfolio project.
No real customers, employees, or transactions are represented.

Files:
- Customers.xlsx: customer master data
- Products.xlsx: product catalog and pricing/cost rates
- Orders.xlsx: order-level facts including revenue, cost, profit, region, and city
- Sales.xlsx: completed sales derived from Orders.xlsx
- Employees.xlsx: employee directory
- Support_Tickets.xlsx: customer support tickets
- Regions.xlsx: region/city lookup table
- Transactions.xlsx: financial transaction records derived from completed sales

Relationships:
- Orders.customer_id -> Customers.customer_id
- Orders.product_id -> Products.product_id
- Sales.order_id -> Orders.order_id
- Sales.customer_id -> Customers.customer_id
- Transactions.sales_id -> Sales.sales_id
- Support_Tickets.customer_id -> Customers.customer_id

Note:
- Data is synthetic and intended for development/testing only.
- A synthetic reduction pattern was introduced for some Chennai Q2 2026 order quantities to support demo analytics.
- Revenue/cost/profit are synthetic values in INR.
