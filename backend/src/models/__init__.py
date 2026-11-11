from .estoque import Estoque
from .logs import Logs
from .produto import EnumUnidadeMedida, EnumAplciacao, Produto
from .usuario import Usuario

from ..db import Base, engine

__all__ = ["Estoque", "EnumUnidadeMedida", "EnumAplciacao", "Produto",
           "Logs", "Usuario"]


#criar todas as tabelas
Base.metadata.create_all(bind=engine)