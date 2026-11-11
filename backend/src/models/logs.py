from sqlalchemy import Column, Integer, ForeignKey, DateTime, BOOLEAN
from sqlalchemy.orm import relationship
from sqlalchemy.exc import now
from datetime import datetime
from ..db import Base


class Logs(Base):
    __tablename__ = "logs"

    idlog = Column(Integer, primary_key=True)
    dt_acao = Column(DateTime, nullable=False, default=now)
    qtn_acao = Column(Integer, nullable=False, unique=True)
    is_retirada = Column(BOOLEAN, nullable=False, default=0)
    estoque_idestoque = Column(Integer ,ForeignKey("estoque.idestoque"), nullable=False)
    usuario_idusuario = Column(Integer ,ForeignKey("usuario.idusuario"), nullable=False)

    usuario = relationship("Usuario", back_populates="logs")
    estoque = relationship("Estoque", back_populates="logs")

    def __init__(self, dt_acao: datetime, qtn_acao: int, estoque_idestoque : int, usuario_idusuario: int, is_retirada: bool =0) -> None:
        self.dt_acao = dt_acao
        self.qtn_acao = qtn_acao
        self.is_retirada = is_retirada
        self.estoque_idestoqueproduto = estoque_idestoque
        self.usuario_idusuario = usuario_idusuario


