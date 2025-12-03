# 🏥 Sistema de Gerenciamento de Pacientes — Clínica Vida+

Projeto acadêmico desenvolvido em Python, voltado ao controle simples de pacientes da Clínica Vida+. O sistema roda no terminal e utiliza uma **lista em memória** para simular um banco de dados.

---

## 📌 Funcionalidades

- Cadastrar pacientes (nome, idade, telefone)
- Listar pacientes cadastrados (ordenados por nome)
- Buscar pacientes por parte do nome
- Exibir estatísticas (total, média de idade, mais novo e mais velho)

---

## 📂 Arquivos

### `bd_mock.py`  
Simula o banco de dados utilizando uma lista de dicionários.

Exemplo real do código:  
```python
def inserir_paciente(nome, idade, telefone):
    PACIENTES.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })
```

### `Menu.py`  
Interface em modo texto contendo o menu principal e as opções de interação com o usuário.
```python
print("1 - Cadastrar")
print("2 - Estatística")
print("3 - Buscar paciente")
print("4 - Listar")
print("5 - Sair")
```

### `tabelas V-F.xlsx`  
Planilha contendo tabelas-verdade com todas as combinações de **A, B, C e D**, utilizadas para modelagem lógica das regras de atendimento: consulta normal e emergência.

---

## ▶️ Como executar

```bash
python Menu.py
```

---

## 🧠 Modelagem Lógica (Resumo)

**Consulta Normal:**  
(A ∧ B ∧ C) ∨ (B ∧ C ∧ D)

**Emergência:**  
C ∧ (B ∨ D)

A planilha inclui **16 linhas** com valores V/F e o resultado das expressões para cada caso.

---

## 🚀 Melhorias futuras

- Persistência dos dados (CSV, SQLite ou JSON)
- Interface gráfica
- Controle de duplicidade (CPF)
- Relatórios mensais

---

## 📜 Licença

Uso educacional e acadêmico. Livre para estudo, modificação e extensão.
