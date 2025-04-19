from fastapi import APIRouter

router = APIRouter(tags=["Appointment book"])


@router.post("/")
def realiza_agendamento():
    pass


@router.get("/")
def lista_agendamentos(ano, mes, dia, ordem):
    pass


@router.get("/{id}")
def detalhes_agendamento():
    pass


@router.patch("/{id}")
def atualiza_agendamento():
    pass


@router.delete("/{id}")
def deleta_agendamento():
    pass


@router.get("/horarios-disponiveis")
def listar_horarios_disponiveis(data, servico):
    pass


@router.get("/{id_cliente}/historico")
def historico_agendamentos():
    pass
