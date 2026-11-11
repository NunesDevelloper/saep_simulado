#CRUD -> dos produtos
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .erros import DuplicationProduto, ErroInesperado, EnumInvalido
from ..models import Produto, EnumUnidadeMedida, EnumAplciacao

def create_prodtudo(nome: str, preco: float, aplicacao: str, unidade_medida: str, 
                    obs: str, session : Session) -> dict:
    try:

        if unidade_medida not in EnumUnidadeMedida : raise EnumInvalido(session)
        if unidade_medida not in EnumAplciacao : raise EnumInvalido(session)

        prodtudo = Produto(nome, preco, aplicacao, unidade_medida, obs)

        session.add(prodtudo)
        session.commit()
        return {'mensagem': 'produto criado com sucesso'}
    
    except IntegrityError:
        raise DuplicationProduto(session)
    
    except Exception as e:
        raise ErroInesperado(e, session)


