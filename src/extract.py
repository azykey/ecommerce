import requests
import pandas as pd
import logging
from datetime import datetime
import json

class DataExtractor:
    def __init__(self, api_config):
        """
        Inicializa extrator com configurações da API
        
        Args:
            api_config (dict): Configurações de conexão
        """
        self.base_url = api_config.get('base_url')
        self.api_key = api_config.get('api_key')
        self.headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }
        
        # Configuração de logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def extract_sales_data(self, endpoint):
        """
        Extrai dados de vendas da API
        
        Args:
            endpoint (str): Endpoint específico para coleta
        
        Returns:
            pd.DataFrame: Dados brutos de vendas
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            data = response.json()
            df = pd.DataFrame(data['sales'])
            
            # Adicionar metadados de extração
            df['extraction_timestamp'] = datetime.now()
            
            self.logger.info(f"Extraídos {len(df)} registros de vendas")
            return df
        
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Erro na extração: {e}")
            return pd.DataFrame()