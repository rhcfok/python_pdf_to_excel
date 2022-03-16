import tabula
import requests
import re
import os 
import urllib

from urllib.parse import urlparse

file_url = ["https://www.cnrl.com/upload/report/133/09/030421-interim_financial_statements.pdf", 
            "https://www.imperialoil.ca/-/media/Imperial/Files/Annual-and-quarterly-reports/2020_q4_earnings_release.pdf",   
            "https://www.cenovus.com/invest/docs/2020/Q4-2020-Interim-Consolidated-Financial-Statements.pdf"]

for i in file_url:
    x = requests.get(i, stream = True)
    a = urlparse(i)
    b = os.path.basename(a.path)
    with open(b,"wb") as pdf:
        for chunk in x.iter_content(chunk_size=1024):
           # writing one chunk at a time to pdf file
             if chunk:
                 pdf.write(chunk)
    tables = tabula.read_pdf(b, pages="all", multiple_tables=True)
    filename = b.replace(".pdf", "")
    tabula.convert_into(b, '{}.csv'.format(filename), pages='all')
    print(filename)
