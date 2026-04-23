import fitz
from pathlib import Path
import pymupdf4llm
import pymupdf

def deconstruct_pdf(pdf_path: Path):
    '''
    Deconstructs a PDF file into its constituent elements, including text, images, and metadata. This function uses the PyMuPDF library to extract information from the PDF file.
    '''
    def extract_txt(pdf_path: Path) -> str:
        return pymupdf4llm.to_markdown(str(pdf_path))
    
    def extract_img(pdf_path: Path) -> list[bytes]:
        imgs = []
        doc = pymupdf.open(str(pdf_path))
        for page in doc:
            for img in page.get_images():
                ref = img[0]
                extract = doc.extract_image(ref)
                imgs.append(extract['image'])
        doc.close()
        return imgs
    return extract_txt(pdf_path), extract_img(pdf_path)

if __name__ == "__main__":
    pdf_path = Path("data/papers/attention_paper.pdf")
    txt, imgs = deconstruct_pdf(pdf_path)
    print(txt[10:20])
    print(len(imgs))