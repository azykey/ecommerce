import pandas as pd
import numpy as np

class DataTransformer:
    @staticmethod
    def clean_sales_data(df):
        """
        Limpa e transforma dados de vendas
        
        Args:
            df (pd.DataFrame): DataFrame de entrada
        
        Returns:
            pd.DataFrame: DataFrame transformado
        """
        # Tratamento de colunas
        columns_mapping = {
            'sale_id': 'sale_id',
            'customer_id': 'customer_id', 
            'product_id': 'product_id',
            'sale_value': 'sale_value',
            'sale_date': 'sale_date'
        }
        df = df.rename(columns=columns_mapping)
        
        # Conversão de tipos
        df['sale_date'] = pd.to_datetime(df['sale_date'])
        df['sale_value'] = df['sale_value'].astype(float)
        
        # Tratamento de valores nulos
        df.fillna({
            'sale_value': 0,
            'customer_id': 'UNKNOWN'
        }, inplace=True)
        
        # Criar colunas derivadas
        df['month'] = df['sale_date'].dt.month
        df['year'] = df['sale_date'].dt.year
        df['quarter'] = df['sale_date'].dt.quarter
        
        # Categorização de vendas
        df['sale_category'] = pd.cut(
            df['sale_value'], 
            bins=[-np.inf, 50, 200, 500, np.inf],
            labels=['Low', 'Medium', 'High', 'Premium']
        )
        
        return df
