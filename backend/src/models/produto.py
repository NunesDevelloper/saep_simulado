from sqlalchemy import Column, Integer, String, DECIMAL, Enum, Text
from sqlalchemy.orm import relationship
from enum import Enum as enum
from ..db import Base


class EnumAplciacao(enum):
    fundacao = "fundação"
    acabamento = "acabamento" 
    estrutura = "estrutura"

class EnumUnidadeMedida(enum):
    kg = "kg"
    m2 = "m2" 
    litros = "litros"
    uni = "uni"

class Produto(Base):
    __tablename__ = "produto"

    idproduto = Column(Integer, primary_key=True)
    preco = Column(DECIMAL(10,2), unique=True, nullable=False)
    nome = Column(String(120), nullable=False, unique=True)
    aplicacao = Column(Enum(EnumAplciacao), nullable=False)
    unidade_medida = Column(Enum(EnumUnidadeMedida), nullable=False, default=EnumUnidadeMedida.uni)
    obs = Column(Text)

    estoque = relationship("Estoque", back_populates="produto",  cascade="all, delete")

    def __init__(self, nome: str, preco: float, aplicacao: EnumAplciacao, obs: str, 
                 unidade_medida: EnumUnidadeMedida = EnumUnidadeMedida.uni) -> None:
        self.nome = nome
        self.preco = preco
        self.aplicacao = aplicacao
        self.obs = obs
        self.unidade_medida = unidade_medida

