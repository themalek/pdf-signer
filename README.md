Wywołanie:
pyton main.py <parametr>

parametr = liczba podpisanych PDFów, czyli 1,2,3... itd.

Generowanie customowego PDFa, który będzie załadowany na stronie 'https://www.digisigner.com/free-electronic-signature/' celem podpisu i uzyskania metadanych na PDF.

Skrypt tworzy lokalizację bazując na ścieżce domowej dodając dalej /development/pdf_script/files (czyli np. /home/twojuser/development/pdf_script/files).
Można to zmienić poprzez ustawienie zmiennych "initialPdfFilePath" i "signedPdfsSavePath".

Inicjalny PDF składać będzie się domyślnie z 3 stron (można zmienić zmienną "pagesInPdf").
