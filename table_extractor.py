import pdfplumber
import pandas as pd
import os

def pdf_to_csv(pdf_path, output_dir, start_page, end_page):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with pdfplumber.open(pdf_path) as pdf:
        for page_num in range(start_page - 1, end_page):  
            page = pdf.pages[page_num]
            tables = page.extract_tables()
            for table_num, table in enumerate(tables):
                df = pd.DataFrame(table[1:], columns=table[0])
                df.reset_index(drop=True, inplace=True)
                csv_filename = f"table_page_{page_num + 1}_table_{table_num + 1}.csv"
                csv_path = os.path.join(output_dir, csv_filename)
                df.to_csv(csv_path, index=False)
                print(f"Saved: {csv_path}")

pdf_path = './input/TSLA-Q2-2024-Update.pdf'
output_dir = 'output_tables'        
start_page = 27                 # Starting page (inclusive)
end_page = 27                   # Ending page (inclusive)
pdf_to_csv(pdf_path, output_dir, start_page, end_page)