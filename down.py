import pandas as pd
import mysql.connector

# MySQL database connection settings
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'students_v13'
}

# Table name
table_name = 'students'

# Connect to MySQL database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Fetch data from the table
query = f"SELECT * FROM {table_name}"
cursor.execute(query)
data = cursor.fetchall()

# Get column names
column_names = [desc[0] for desc in cursor.description]

# Create a DataFrame
df = pd.DataFrame(data, columns=column_names)

# Close database connection
cursor.close()
conn.close()

# Export to CSV
csv_filename = 'students.csv'
df.to_csv(csv_filename, index=False)

# Export to Excel
excel_filename = 'students.xlsx'
df.to_excel(excel_filename, index=False)

print(f'Data has been exported to {csv_filename} and {excel_filename}.')
