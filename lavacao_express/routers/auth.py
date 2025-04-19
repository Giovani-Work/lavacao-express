from fastapi import APIRouter

router = APIRouter(tags=["Auth"])


@router.post("/login")
def login_usuario():
    pass


@router.post("/change-password")
def alterar_senha(id_usuario: int):
    pass
