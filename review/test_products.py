from review.products import ListProduct
from review.product import Product

lp=ListProduct()
lp.add_product(Product(id=100, name="Product 1", quantity= 200, price=10))
lp.add_product(Product(id=200, name="Product 2", quantity= 10, price=15))
lp.add_product(Product(id=150, name="Product 3", quantity= 80, price=8))
lp.add_product(Product(id=300, name="Product 4", quantity= 50, price=20))
lp.add_product(Product(id=250, name="Product 5", quantity= 150, price=17))
print("List of Products:")
lp.print_products()
print("List of Products after descending sort: ")
lp.desc_sort_products()
lp.print_products()