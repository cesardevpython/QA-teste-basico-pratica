# QA_PYTEST_BASICO

Projeto básico de testes automatizados com **Python** e **Pytest**, criado para validar funções matemáticas e manipulação de strings.

## 📁 Estrutura do Projeto

```
QA_PYTEST_BASICO/
├── assets/                      # Pasta para assets (relatórios, evidências, etc.)
├── funcoes_mat.py              # Funções que serão testadas
├── test_calculadora.py         # Testes relacionados a uma calculadora
├── test_calculadora2.py        # Segundo arquivo de testes (variações)
├── test_funcoes_mat.py         # Testes das funções do arquivo funcoes_mat.py
├── relatorio_teste.html        # Relatório em HTML gerado com pytest-html
├── Resultado_teste.txt         # Relatório em texto com resultados dos testes
└── requirements.txt            # (opcional) Dependências do projeto
```

## ⚙️ Requisitos

- Python 3.8+
- pip

## 🛠️ Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/QA_PYTEST_BASICO.git
cd QA_PYTEST_BASICO
```

2. Instale o `pytest` (e `pytest-html`, se quiser gerar relatórios):

```bash
pip install pytest pytest-html
```

> Se quiser, salve as dependências:
> ```bash
> pip freeze > requirements.txt
> ```

## 🧪 Executando os Testes

### Testes comuns:

```bash
pytest
```

### Testes com mais detalhes:

```bash
pytest -v
```

### Gerar relatório em HTML:

```bash
pytest --html=relatorio_teste.html
```

O relatório será salvo na raiz do projeto e pode ser aberto no navegador.

## 🧠 Funções que estão sendo testadas

Arquivo: `funcoes_mat.py`

```python
def dividir(a, b):
    return a / b

def subtrair(a, b):
    return a + b  # <- propositalmente com erro para teste

def eh_par(numero):
    return numero % 2 == 0

def raiz_quadrada(n):
    return n ** (1/2)

def inverter_string(s):
    return s[::-2]
```

> A função `subtrair(a, b)` está com erro de lógica proposital para ilustrar falha em teste.

## 🧪 Exemplo de Teste

Arquivo: `test_funcoes_mat.py`

```python
from funcoes_mat import subtrair

def test_subtrair():
    assert subtrair(6, 2) == 4
```

## 📄 Licença

Este projeto é livre para fins educacionais.
