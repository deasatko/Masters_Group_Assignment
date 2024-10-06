import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

file_path = './data/final_cleaned.csv'
data = pd.read_csv(file_path)

# Group by main_category and calculate the average rating
avg_rating_by_category = data.groupby('main_category')['ratings'].mean().sort_values(ascending=False)

# Creating a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_rating_by_category.index, y=avg_rating_by_category.values, palette="viridis")
plt.title('Average Rating by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''
The bar chart compares the average customer satisfaction (ratings) across different product categories. 
Clients want to know which categories have higher customer satisfaction so they can promote them more effectively.
Helps identify categories where products are performing well or poorly in terms of customer ratings.
'''


# Creating a box plot to show ratings distribution by category
plt.figure(figsize=(12, 6))
sns.boxplot(x='main_category', y='ratings', data=data, palette="Set3")
plt.title('Ratings Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Ratings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''
Box plots are ideal for displaying the spread of ratings within each category. 
This graph helps Amazon identify how varied or consistent customer experiences are within categories.
Categories with a wide range of ratings could indicate inconsistent product quality, while narrower ranges could indicate more consistent satisfaction.
'''



# Create histogram for discounted prices, this will open a web tab.
fig = px.histogram(data, x='discount_price', nbins=20, title="Distribution of Discounted Prices",
labels={'discount_price':'Discounted Price'}, 
template="plotly_dark")

# Update layout
fig.update_layout(xaxis_title="Discounted Price", yaxis_title="Frequency")
fig.show()

'''
The histogram visualizes the spread of product prices, showing how products are priced after discounting. 
This is useful for clients who want to understand the range of product prices.
Identifies pricing strategies and helps customers find affordable products or compare which categories offer more competitive pricing.
'''


# Create a scatter plot for number of ratings vs discounted price
fig = px.scatter(data, x='discount_price', y='no_of_ratings', color='main_category', 
title="Number of Ratings vs. Discounted Price",
labels={'discount_price':'Discounted Price', 'no_of_ratings':'Number of Ratings'},
template="plotly")

# Update layout
fig.update_layout(xaxis_title="Discounted Price", yaxis_title="Number of Ratings")
fig.show()

'''
The scatter plot helps to see if there is a relationship between product pricing (discounted price) and customer engagement (number of reviews/ratings).
If products with higher discounts receive more ratings, Amazon could use this to encourage customer engagement by offering discounts on certain items.
'''


# Final Summary:

# Bar Chart (Seaborn: Average Rating by Product Category) – Shows which categories receive higher customer satisfaction ratings, helping Amazon target those for promotions or product improvements.

# Box Plot (Seaborn: Ratings Distribution by Category) – Helps to visualize the variability in customer ratings within each product category, showing where consistency or inconsistency in quality exists.

# Histogram (Plotly: Distribution of Discounted Prices) – Shows the range of product prices after discounts, helping clients understand the affordability of products across categories.

# Scatter Plot (Plotly: Number of Ratings vs. Discounted Price) – Highlights the relationship between product price and customer engagement (through ratings), helping identify how pricing strategies influence reviews.

# These visualizations provide insights into customer satisfaction, pricing, and engagement trends, which are crucial for Amazon and its stakeholders to make informed decisions.