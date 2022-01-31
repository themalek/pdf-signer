**Instalacja:**

_pip install -r requirements.txt_

lub

_pip3 install -r requirements.txt_


**Wywołanie:**

_python main.py **parametr**_

lub

_python3 main.py **parametr**_

**parametr** = liczba podpisanych PDFów, czyli 1,2,3... itd.

Generowanie customowego PDFa, który będzie załadowany na stronie 'https://www.digisigner.com/free-electronic-signature/' celem podpisu i uzyskania metadanych na PDF.

Skrypt tworzy lokalizację bazując na ścieżce domowej dodając dalej /development/pdf_script/files (czyli np. /home/user/development/pdf_script/files).
Można to zmienić poprzez ustawienie zmiennych **initialPdfFilePath** i **signedPdfsSavePath**.

Inicjalny PDF składać będzie się domyślnie z 3 stron (można zmienić zmienną **pagesInPdf**).
