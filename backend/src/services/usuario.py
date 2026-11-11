#CRUD -> dos usarios
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .erros import DuplicationUser, ErroInesperado, NoteUserSenha, RequestInvalida
from ..models import Usuario

def create_user(nome: str, senha: str, email: str, session : Session) -> dict:
    try:
        user = Usuario(nome, email, senha)

        session.add(user)
        session.commit()
        return {'mensagem': 'cliente criado com sucesso'}
    
    except IntegrityError:
        raise DuplicationUser(session)
    
    except Exception as e:
        raise ErroInesperado(e, session)

def dellet_user(id: int, session: Session) -> dict:
    try:

        query = session.query(Usuario).filter_by(idusuario = id).delete() 

        if query:
            session.commit()
            return {"mensagem": "cliente removido."}
        else: raise NoteUserSenha(session)

    #relançar o erro 
    except (NoteUserSenha) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def update_user(id: int, senha: str  | None, nome: str | None, session: Session) -> dict:
    try:
        query = session.query(Usuario).filter_by(idusuario = id).first()

        if query:
            if senha != None :  query.novaSenha(senha)  
             
            if nome != None: query.nome = nome 

            if nome is None and senha is None: raise RequestInvalida(session)

        else: raise NoteUserSenha(session)

        session.commit()
        return {'mensagem': 'cliente editado com sucesso.'}

    except (NoteUserSenha, RequestInvalida) : raise

    except Exception as e:
        raise ErroInesperado(e, session)

def read_user(id: int, session: Session) -> dict:
    try:
        query = session.query(Usuario).filter_by(idusuario = id).first()

        if query is not None:
            return {
                'mensagem':{
                    'nome' : query.nome,
                    'email' : query.email
                }
            }
        else: raise NoteUserSenha(session)
    
    except (NoteUserSenha): raise

    except Exception as e:
        raise ErroInesperado(e, session)   

