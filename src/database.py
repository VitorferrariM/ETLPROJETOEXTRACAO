from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BitcoinPreco(Base):
    __tablename__ = 'bitcoin_precos'
    
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    criptomoeda = Column(String)
    moeda = Column(String)
    timestamp = Column(DateTime)
