import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="winery",
        password="grapes",
        database="project_bacchus"
    )

def run_employee_hours_report():

    connection = connect_to_db()
    cursor = connection.cursor()

    print("\n---- EMPLOYEE HOURS REPORT ----\n")

    query = """
        SELECT 
            e.first_name,
            e.last_name,
            d.dept_name,
            eh.year,
            eh.quarter,
            eh.hours_worked
        FROM employee_hour eh
        JOIN employee e ON eh.employee_id = e.employee_id
        JOIN department d ON e.dept_id = d.dept_id
        ORDER BY e.last_name, eh.year, eh.quarter;
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("Employee | Dept | Year | Quarter | Hours Worked")
    print("=" * 75)

    for r in rows:
        full_name = f"{r[0]} {r[1]}"
        print(f"{full_name} | {r[2]} | {r[3]} | {r[4]} | {r[5]}")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    run_employee_hours_report()
