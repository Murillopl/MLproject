import os
from src.components.data_ingestion import DataIngestion

def run_training_pipeline():
    data_ingestion = DataIngestion()
    data_ingestion.initiate_data_ingestion()

if __name__ == "__main__":
    run_training_pipeline()
