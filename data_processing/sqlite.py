# import sqlite3
# import pandas as pd
#
# try:
#     sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
#     cursor = sqliteConnection.cursor()
#     print("DB Init")
#     query= 'SELECT * FROM InvoiceLine LIMIT 5;'
#     cursor.execute(query)
#     df = pd.DataFrame(cursor.fetchall())
#     print(df)
#     cursor.close()
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection closed")

import sqlite3
import pandas as pd
def top_n_customers(n: int):
    try:
        sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
        df_customers = pd.read_sql_query("SELECT * FROM Customer;", sqliteConnection)
        df_invoices = pd.read_sql_query("SELECT * FROM Invoice;", sqliteConnection)
        merged_df = pd.merge(df_customers, df_invoices, on="CustomerId")
        top_customers = (
            merged_df.groupby(["CustomerId", "FirstName", "LastName"])["Total"]
            .sum()
            .reset_index()
            .sort_values(by="Total", ascending=False)
            .head(n)
        )
        return top_customers
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
n = int(input("Nhập số lượng customer top N: "))
result = top_n_customers(n)
print(f"Top {n} customer có giá trị mua hàng cao nhất:")
print(result)
