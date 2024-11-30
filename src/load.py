from sqlalchemy import create_engine, Column, Float, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales_data'
    
    sale_id = Column(String, primary_key=True)
    customer_id = Column(String)
    product_id = Column(String)
    sale_value = Column(Float)
    sale_date = Column(DateTime)
    month = Column(Integer)
    year = Column(Integer)
    quarter = Column(Integer)
    sale_category = Column(String)

class DataLoader:
    def __init__(self, connection_string):
        """
        Inicializa carregador de dados
        
        Args:
            connection_string (str): String de conexão do banco
        """
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        
        self.Session = sessionmaker(bind=self.engine)
        
        # Configuração de logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def load_to_database(self, df):
        """
        Carrega DataFrame no banco de dados
        
        Args:
            df (pd.DataFrame): DataFrame a ser carregado
        """
        session = self.Session()
        
        try:
            # Converter DataFrame para lista de dicionários
            records = df.to_dict('records')
            
            # Inserir dados
            for record in records:
                sale = Sale(**record)
                session.merge(sale)
            
            session.commit()
            self.logger.info(f"Carregados {len(records)} registros")
        
        except Exception as e:
            self.logger.error(f"Erro no carregamento: {e}")
            session.rollback()
        finally:
            session.close()