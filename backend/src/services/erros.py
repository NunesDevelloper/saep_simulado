from fastapi import HTTPException, status
from sqlalchemy.orm import Session


#region erros user
class DuplicationUser(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='já existe um cliente com esse email'
        )

class NoteUserSenha(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há User com esse Email"
        )

#endregion

#region erros produto
class DuplicationProduto(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='já existe um cliente com esse email'
        )

class NoteProduto(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há User com esse Email"
        )

#endregion

#region logs
class NoteFoundLogs(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há log com esse id"
        )

class NoteAllLogs(HTTPException):
    def __init__(self, session: Session):
        session.rollback()

        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Não há log no banco"
        )

#endregion

#region erros Gerais
class ErroInesperado(HTTPException):
    def __init__(self, e, session: Session | None = None):
        if session is not None:
            session.rollback()

        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro inesperado do servidor.Erro -> {e}"
        )

class RequestInvalida(HTTPException):
    def __init__(self, session: Session | None = None):
        
        if session is not None: session.rollback()

        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail= "Nem um campo devidamente informado"
        )


class EnumInvalido(HTTPException):
    def __init__(self, session: Session | None = None):
        
        if session is not None: session.rollback()

        super().__init__(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail= "Não há essa opeção"
        )

#endregion