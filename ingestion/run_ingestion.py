from ingestor import Ingestor
import os

if __name__ == "__main__":
    v_path = os.path.abspath("vault")
    ingestor = Ingestor(v_path)
    pdf_path = os.path.abspath("reactor modelling.pdf")
    print(f"Ingesting: {pdf_path}")
    result = ingestor.ingest(pdf_path)
    print(f"Ingestion result: {result}")
