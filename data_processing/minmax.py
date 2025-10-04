# import pandas as pd
#
# def find_orders_within_range(df : pd.DataFrame, minValue, maxValue):
#     order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
#     orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]
#     unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
#     return unique_orders
# df = pd.read_csv('../datasets/SalesTransactions.csv')
# minValue = float(input("Nhập giá trị min: "))
# maxValue = float(input("Nhập giá trị max: "))
# result = find_orders_within_range(df, minValue, maxValue)
# print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, 'là:', result)

import pandas as pd
def top3_products(df: pd.DataFrame):
    product_totals = df.groupby('ProductID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())
    top3 = product_totals.sort_values(ascending=False).head(3)
    return top3
df = pd.read_csv('../datasets/SalesTransactions.csv')
result = top3_products(df)
print("Top 3 sản phẩm bán ra có giá trị lớn nhất là:")
print(result)
