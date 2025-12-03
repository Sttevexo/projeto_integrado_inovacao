

# Lista simulando um banco de dados em memória
PACIENTES = []



def inserir_paciente(nome, idade, telefone):
    PACIENTES.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })


def listar_pacientes():
    # Ordena por nome
    return sorted(
        [(p["nome"], p["idade"], p["telefone"]) for p in PACIENTES],
        key=lambda x: x[0].lower()
    )


def estatisticas_pacientes():
    total = len(PACIENTES)
    if total == 0:
        return 0, 0, None, None

    # Média de idades
    media = sum(p["idade"] for p in PACIENTES) / total

    # Mais velho
    p_mais_velho = max(PACIENTES, key=lambda p: p["idade"])
    mais_velho = (p_mais_velho["nome"], p_mais_velho["idade"], p_mais_velho["telefone"])

    # Mais novo
    p_mais_novo = min(PACIENTES, key=lambda p: p["idade"])
    mais_novo = (p_mais_novo["nome"], p_mais_novo["idade"], p_mais_novo["telefone"])

    return total, media, mais_novo, mais_velho


def buscar_pacientes_por_nome(nome):
    termo = nome.lower()
    resultado = [
        (p["nome"], p["idade"], p["telefone"])
        for p in PACIENTES
        if termo in p["nome"].lower()
    ]

    return sorted(resultado, key=lambda x: x[0].lower())
