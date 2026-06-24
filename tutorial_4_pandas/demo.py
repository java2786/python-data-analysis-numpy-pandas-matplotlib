import pandas as pd

inventory = pd.DataFrame({
    'Product': ['Mobile', 'Laptop', 'Shirt'],
    'Quantity': [12, 4, 5],
    'Price': [12999, 65000, 500],
    'Category': ['Electorinc','Electorinc','Cloth']
})

print(inventory)