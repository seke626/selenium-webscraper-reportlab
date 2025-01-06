import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

driver_path = "webdriver-path" #replace with your own Chrome webdriver path
options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=driver_path, options=options)

url = 'https://www.bbc.co.uk/news'

driver.get(url)

time.sleep(2)

headlines = driver.find_elements(By.CSS_SELECTOR, 'h3 a')

headlines_list = [headline.text.strip() for headline in headlines if headline.text.strip()]

pdf_filename = 'bbc_news_headlines.pdf'
c = canvas.Canvas(pdf_filename, pagesize=letter)

c.setFont("Helvetica", 12)
x, y = 40, 750

c.setFont("Helvetica-Bold", 16)
c.drawString(x, y, "BBC News Headlines")
y -= 30

c.setFont("Helvetica", 12)
for headline in headlines_list:
    if y < 40:
        c.showPage()
        c.setFont("Helvetica", 12)
        y = 750
    c.drawString(x, y, f"- {headline}")
    y -= 15

c.save()

driver.quit()

print(f"PDF saved as {pdf_filename}")
