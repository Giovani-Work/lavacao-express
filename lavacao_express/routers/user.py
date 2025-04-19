from fastapi import APIRouter

router = APIRouter(tags=["User"])


@router.post("/")
def cadastro_de_usuario():
    pass


@router.get("/{id_usuario}")
def detalhes_do_conta(id_usuario: int):
    pass

