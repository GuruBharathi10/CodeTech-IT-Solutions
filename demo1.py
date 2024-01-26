from bs4 import BeautifulSoup
import openpyxl

# Read the HTML file
with open('Amazon.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with the specified class
divs = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2rh3j15wdcp4q29xeaptoa72x6 s-latency-cf-section puis-card-border')

# Create an Excel workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write headers to the Excel sheet
sheet.append(['Product_Name', 'Product_Price', 'Product_Reviews'])

# Loop through each div and extract information
for div in divs:
    # Find Product_Name
    product_name_span = div.find('span', class_='a-size-medium a-color-base a-text-normal')
    product_name = product_name_span.text.strip() if product_name_span else " "

    # Find Product_Price
    product_price_span = div.find('span', class_='a-price-whole')
    product_price = product_price_span.text.strip() if product_price_span else " "

    # Find Product_Reviews
    product_reviews_span = div.find('span', class_='a-size-base s-underline-text')
    product_reviews = product_reviews_span.text.strip() if product_reviews_span else " "

    # Write data to Excel sheet
    sheet.append([product_name, product_price, product_reviews])

# Save the Excel file
workbook.save('Amazon_Products.xlsx')
