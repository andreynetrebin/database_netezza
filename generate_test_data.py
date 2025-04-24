from faker import Faker
import random
import pandas as pd

fake = Faker()

# Количество записей для генерации
num_sales = 1000000
num_products = 200000
num_customers = 500000

# Генерация данных для таблицы products
products = []
for i in range(num_products):
    product = {
        'product_id': i + 1,
        'product_name': fake.word(),
        'category': fake.word(),
        'price': round(random.uniform(10.0, 100.0), 2)
    }
    products.append(product)

# Генерация данных для таблицы customers
customers = []
for i in range(num_customers):
    customer = {
        'customer_id': i + 1,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'phone': fake.phone_number()
    }
    customers.append(customer)

# Генерация данных для таблицы sales
sales = []
for i in range(num_sales):
    sale = {
        'sale_id': i + 1,
        'product_id': random.randint(1, num_products),
        'customer_id': random.randint(1, num_customers),
        'sale_date': fake.date_this_year(),
        'amount': round(random.uniform(50.0, 500.0), 2),
        'quantity': random.randint(1, 10)
    }
    sales.append(sale)

# Создание DataFrame для каждой таблицы
products_df = pd.DataFrame(products)
customers_df = pd.DataFrame(customers)
sales_df = pd.DataFrame(sales)

# Сохранение данных в CSV файлы (или можно использовать для вставки в базу данных)
products_df.to_csv('products.csv', index=False)
customers_df.to_csv('customers.csv', index=False)
sales_df.to_csv('sales.csv', index=False)

print("Данные успешно сгенерированы и сохранены в CSV файлы.")
