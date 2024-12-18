import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import uuid
import json

def initialize_chromadb():
    client = chromadb.PersistentClient('vectorstore')
    return client.get_or_create_collection("invoice_data")

def ingest_data(collection, data):
    if isinstance(data, list) and all(isinstance(record, dict) for record in data):
        for record in data:
            try:
                document = f"""
                Vendor: {record['vendor_name']}
                Contract Name: {record['contract_name']}
                Invoice Number: {record['invoice_number']}
                Project Name: {record['summary_text']['project_name']}
                Total Amount: {record['summary']['total_completed_and_stored_to_date']}
                """
                metadata = {"id": record["id"], "project_id": record["project_id"]}
                collection.add(documents=[document], metadatas=[metadata], ids=[str(uuid.uuid4())])
            except KeyError as e:
                print(f"Skipping record due to missing field: {str(e)}")
            except Exception as e:
                print(f"Error ingesting record: {str(e)}")
    else:
        raise ValueError("Invalid data format: Expected a list of dictionaries")


