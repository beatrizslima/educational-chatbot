import pymupdf

doc = pymupdf.open('Livro_Portugues.pdf')  # or pymupdf.Document(filename)
page = doc.load_page(15)
text = page.get_text()
toc = doc.get_toc()
print(page)
print(page.rect)