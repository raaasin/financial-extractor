import pdfplumber
import pandas as pd
import re

input_pdf = './input/TSLA-Q2-2024-Update.pdf'

def find_financial_statements_page(pdf):
    for page_num in range(5):  # Assuming index is in the first 5 pages
        page = pdf.pages[page_num]
        text = page.extract_text()
  
        match = re.search(r'Financial Statements\s+(\d+)', text, re.IGNORECASE)
        if match:
            financial_statements_page = int(match.group(1))
            #print(f"Found 'Financial Statements' on page {page_num + 1}, listed to be on page {financial_statements_page}")
            return financial_statements_page

    return None

with pdfplumber.open(input_pdf) as pdf:
    financial_statements_page = find_financial_statements_page(pdf)

if financial_statements_page:
    print(f"'Financial Statements' starts on page: {financial_statements_page}")
else:
    print("Could not find 'Financial Statements' in the index.")