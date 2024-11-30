import os
from dotenv import load_dotenv
from extract import DataExtractor
from transform import DataTransformer
from load import DataLoader

def main():
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Configurações
    API_CONFIG = {
        'base_url': os.getenv('API_BASE_URL'),
        'api_key': os.getenv('API_KEY')
    }
    DB_CONNECTION = os.getenv('DATABASE_URL')
    
    # Inicializar componentes
    extractor = DataExtractor(API_CONFIG)
    transformer = DataTransformer()
    loader = DataLoader(DB_CONNECTION)
    
    try:
        # Pipeline ETL
        raw_data = extractor.extract_sales_data('sales')
        transformed_data = transformer.clean_sales_data(raw_data)
        loader.load_to_database(transformed_data)
        
        print("Pipeline ETL executado com sucesso!")
    
    except Exception as e:
        print(f"Erro no pipeline ETL: {e}")

if __name__ == "__main__":
    main()