from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from argon2 import PasswordHasher
from ..db import Base

#objeto para gera e verificar os hash
ph = PasswordHasher()

class Usuario(Base):
    __tablename__ = "usuario"

    idusuario = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    senha = Column(String(225), nullable=False)
    nome = Column(String(120), nullable=False)

    logs = relationship("Logs", back_populates="usuario", cascade="all, delete")
    
    def __init__(self, email: str, senha: str, nome: str) -> None:
        self.email = email
        self.senha = ph.hash(senha)
        self.nome = nome


    def verificar_senha(self, senha: str) -> bool:
        return ph.verify(hash=self.senha, password=senha)

    def nova_senha(self, senha: str) -> None:
        self.senha = ph.hash(senha)