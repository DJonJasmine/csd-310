import mysql.connector

def connect_to_db():
    """Create a database connection and return the connection and cursor."""
    connection = mysql.connector.connect(
        host="localhost",
        user="winery",
        password="grapes",
        database="project_bacchus"
    )
    return connection, connection.cursor()

def display_records(cursor, table):
    """Query a table and print its records and column names."""
    cursor.execute(f"SELECT * FROM {table}")
    results = cursor.fetchall()
    column_headers = [col[0] for col in cursor.description]

    print(f"\nDisplaying {table} table\n")
    print(" | ".join(column_headers))
    print("".join(["="] * 60))

    for row in results:
        formatted_row = " | ".join(str(item) for item in row)
        print(formatted_row)
    print()

def main():
    tables_to_show = [
        "department",
        "employee",
        "employee_hours",
        "supplier",
        "distributor",
        "product",
        "inventory",
        "shipment",
        "shipment_detail"
    ]

    connection, cursor = connect_to_db()

    for table in tables_to_show:
        display_records(cursor, table)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
