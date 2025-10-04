from review.product import Product

p1=Product(id=100,name="Thuốc lào", quantity=4, price=20)
print(p1)
p2=Product(id=200, name="Thuốc trị hôi nách", quantity=5, price=30)
p1=p2
print("Thông tin của p1=")
print(p1)
p1.name="Thuốc tăng tự trọng"
print("Thông tin của p2=")
print(p2)