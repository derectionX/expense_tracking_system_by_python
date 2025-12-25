import mysql.connector
from contextlib import contextmanager

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager",
        port=3306
    )


@contextmanager
def get_db_cursor(commit=False):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()


# ------------------------------------------
# FETCH EXPENSES FOR A SPECIFIC DATE
# ------------------------------------------
def fetch_expenses_for_date(expense_date):
    logger.info(f"fatch_expenses_for_date called with {expense_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT * FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )
        expenses = cursor.fetchall()
        return expenses


# ------------------------------------------
# INSERT EXPENSE
# ------------------------------------------
def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount:{amount},category: {category},notes: {notes}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (%s, %s, %s, %s)
            """,
            (expense_date, amount, category, notes)
        )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_epenses_for_date called with {expense_date}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM expenses WHERE expense_date = %s",
            (expense_date,)
        )

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fatch_expense_summary called with start: {start_date}, end: {end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            ''' SELECT category,SUM(amount) AS total
                FROM expenses WHERE expense_date 
                BETWEEN %s AND %s
                GROUP BY category;'''
            ,
            (start_date,end_date)
        )
        data = cursor.fetchall()
        return data


if __name__ == "__main__":

    ex = fetch_expenses_for_date("2024-09-30")
    print(ex)

    #delete_expenses_for_date("2024-08-25")

    summary = fatch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)

