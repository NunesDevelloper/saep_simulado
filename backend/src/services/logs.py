from sqlalchemy.orm import Session

from .erros import ErroInesperado, NoteFoundLogs
from ..models import Logs

def read_user(id: int, session: Session) -> dict:
    try:
        query = session.query(Logs).filter_by(idusuario = id).first()

        if query is not None:
            return {
                'mensagem':{
                    'dt_acao' : query.dt_acao,
                    'qtn_acao' : query.qtn_acao,
                    'is_retirada': query.is_retirada
                }
            }
        else: raise NoteFoundLogs(session)
    
    except (NoteFoundLogs): raise

    except Exception as e:
        raise ErroInesperado(e, session)   

