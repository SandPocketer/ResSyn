
from pdf_extractor import deconstruct_pdf
from pathlib import Path
import re

def chunk(mkd_txt: str, chunk_size: int = 1000) -> list[str]:
    '''
    Chunks preprocessed txt date using mkdown headers
    '''
    chunks = []
    sections = re.split(r'\n(?=#)', mkd_txt)
    for chunk in sections:
        lines = chunk.strip().split('\n')
        try:
            chunk = {'header': chunk.split('**')[1], \
                    'content': chunk.split('**')[2] if len(chunk.split('**')) > 2 else ''}
        except IndexError:
            continue
        chunks.append(chunk)
    
    return chunks

if __name__ == "__main__":
    pdf_path = Path("data/papers/attention_paper.pdf")
    mkd_txt, _ = deconstruct_pdf(pdf_path)
    chunks = chunk(mkd_txt)
    print(chunks[1])