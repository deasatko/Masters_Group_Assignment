import pandas as pd

products_dataset_path = 'data/Amazon-Products.csv'
df = pd.read_csv(products_dataset_path)

columns_to_keep = [
    'name',
    'main_category',
    'sub_category',
    'ratings',
    'no_of_ratings',
    'discount_price',
    'actual_price'
]
df_cleaned = df[columns_to_keep]

print("Cleaned DataFrame:")
print(df_cleaned.head())

cleaned_dataset_path = 'data/original_data.csv'
df_cleaned.to_csv(cleaned_dataset_path, index=True)

print(f"Cleaned dataset saved to {cleaned_dataset_path}")
