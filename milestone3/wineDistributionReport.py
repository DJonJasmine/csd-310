import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="winery",
        password="grapes",
        database="project_bacchus"
    )

def run_wine_distribution_report():
    """Generate wine distribution report grouped correctly for MySQL strict mode."""

    connection = connect_to_db()
    cursor = connection.cursor()

    print("\n---- WINE DISTRIBUTION REPORT ----\n")

    query = """
        SELECT 
            p.wine_type,
            d.distributor_name,
            SUM(sd.quantity) AS total_quantity,
            SUM(sd.quantity * sd.unit_price) AS revenue
        FROM shipment_detail sd
        JOIN shipment sh ON sd.shipment_id = sh.shipment_id
        JOIN product p ON sd.product_id = p.product_id
        JOIN distributor d ON sh.distributor_id = d.distributor_id
        GROUP BY p.wine_type, d.distributor_name
        ORDER BY p.wine_type, d.distributor_name;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("Wine Type | Distributor | Quantity Sold | Revenue")
    print("=" * 70)

    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | ${r[3]:,.2f}")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    run_wine_distribution_report()
