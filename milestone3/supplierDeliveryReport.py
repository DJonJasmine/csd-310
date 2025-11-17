import mysql.connector

def connect_to_db():
    """Establish and return MySQL connection and cursor."""
    conn = mysql.connector.connect(
        host="localhost",
        user="winery",
        password="grapes",
        database="project_bacchus"
    )
    return conn, conn.cursor()

def run_supplier_delivery_report():
    """Query and display supplier delivery performance."""
    conn, cursor = connect_to_db()

    query = """
        SELECT 
            s.Supplier_Name,
            sh.Expected_Delivery,
            sh.Actual_Delivery,
            DATEDIFF(sh.Actual_Delivery, sh.Expected_Delivery) AS Days_Late,
            MONTH(sh.Expected_Delivery) AS Delivery_Month
        FROM Shipment sh
        JOIN Supplier s ON sh.Supplier_ID = s.Supplier_ID
        ORDER BY sh.Expected_Delivery;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n---- SUPPLIER DELIVERY PERFORMANCE REPORT ----\n")
    print("Supplier | Expected | Actual | Days Late | Month\n")
    print("=" * 70)

    for row in results:
        print(row)

    cursor.close()
    conn.close()

run_supplier_delivery_report()
