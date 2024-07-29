from pypdf import PdfReader
 
def extract_information(pdf_path):
    reader = PdfReader("Livro_Portugues.pdf")
    number_of_pages = len(reader.pages)
    page = reader.pages[16]
    info = reader.metadata
    text = page.extract_text(extraction_mode="layout")

    txt = f"""
    Information about {pdf_path}: 
    Info: {info}
    Number of pages: {number_of_pages}
    Text: {text}
    """

    print(txt)

# if __name__ == '__main__':
path = 'Livro_Portugues.pdf'
extract_information(path)