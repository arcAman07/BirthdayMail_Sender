import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv("C:/Users/amans/Downloads/DSC Task 1 - Absenteeism_at_work.csv")
df = pd.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect(
    "Driver={node-reference};"
    "Server=RON\SQLEXPRESS;"
    "Database=test_database;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Create Table
cursor.execute(
    """
		CREATE TABLE mails (
			idmails int primary key,
			name nvarchar(50),
			email nvarchar(100),
			)
               """
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        """
                INSERT INTO products (idmails, name, email)
                VALUES (?,?,?)
                """,
        row.idmails,
        row.names,
        row.email,
    )
conn.commit()
