from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Estoque(Base):
    __tablename__ = "estoque"

    idestoque = Column(Integer, primary_key=True)
    qtn_minima = Column(Integer, nullable=False)
    qtn = Column(Integer, nullable=False, unique=True)
    produto_idproduto = Column(Integer ,ForeignKey("produto.idproduto"), nullable=False)

    produto = relationship("Produto", back_populates="estoque")
    logs = relationship("Logs", back_populates="estoque", cascade="all, delete")

    def __init__(self, qtn_minima: int, qtn: int, roduto_idproduto : int) -> None:
        self.qtn_minima = qtn_minima
        self.qtn = qtn
        self.roduto_idproduto = roduto_idproduto


