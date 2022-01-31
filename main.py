import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import fpdf
import datetime
from pathlib import Path

pagesInPdf = 3
pdfsAmount = 10
currentDateString = datetime.datetime.now().strftime('%Y%m%d')
initialPdfFilePath = f"{str(Path.home())}/development/pdf_script/files/{currentDateString}/{currentDateString}.pdf"
signedPdfsSavePath = f"{str(Path.home())}/development/pdf_script/files/{currentDateString}"


def start():
    try:
        os.makedirs(name=signedPdfsSavePath, mode=0o777)
    except OSError as error:
        print(f">>>>>> {error}")
    createPDF()
    for x in range(pdfsAmount):
        createAndDownloadSignedDocument()


def createPDF():
    pdf = fpdf.FPDF(format='letter')
    for x in range(pagesInPdf):
        pdf.add_page()
        pdf.set_font("Arial", size=24)
        pdf.cell(200, 10, txt=currentDateString, ln=1, align="L")
    pdf.output(initialPdfFilePath)
    print(f"Stworzono podstawowy PDF w ścieżce {initialPdfFilePath}")


def createAndDownloadSignedDocument():
    url = 'https://www.digisigner.com/free-electronic-signature/'
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": signedPdfsSavePath}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    fileInput = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    fileInput.send_keys(initialPdfFilePath)

    sleep(1)

    signDocumentArea = driver.find_element(By.ID, 'page-0')
    signDocumentArea.click()

    sleep(1)

    textInputToSign = driver.find_element(By.ID, 'signatureTextInput')
    textInputToSign.send_keys('Random word')

    sendButton = driver.find_element(By.CSS_SELECTOR, 'button[translate="OK_BUTTON"]')
    sendButton.click()

    sleep(1)

    doneButton = driver.find_element(By.ID, 'singButton')
    doneButton.click()

    sleep(3)

    downloadButton = driver.find_element(By.ID, 'downloadDocumentButton')
    downloadButton.click()

    print(f"Pobrano podpisany plik PDF do ścieżki {signedPdfsSavePath}")
    driver.close()
    driver.quit()


if __name__ == "__main__":
    try:
        pdfsAmount = int(sys.argv[1])
    except:
        print(f"Niepoprawny parametr dla ilości PDF. Utworzone zostanie {pdfsAmount} PDF/ów.")
    start()
