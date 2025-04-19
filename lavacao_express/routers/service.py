from fastapi import APIRouter

router = APIRouter(tags=["Services"])


@router.get("/")
def listar_servicos_disponiveis():
    pass


@router.post("/")
def cadastrar_servico():
    pass
