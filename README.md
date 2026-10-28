# Gráficos das Funções de Ativação

Esse projeto foi feito para a atividade de Redes Neurais Artificiais (RNA). Trata-se de um script em Python que desenha o gráfico de cada função de ativação que vimos em aula, para mostrar na prática como a curva muda quando alteramos os parâmetros.

## O que o código faz

O código plota 7 funções de ativação. Cada uma aparece com 3 valores diferentes de parâmetro, assim dá para comparar as curvas no mesmo gráfico.

**Funções totalmente diferenciáveis** (têm derivada em todos os pontos):

| Função | Parâmetro que varia | O que ele muda |
|---|---|---|
| Logística | β | A inclinação da curva |
| Tangente hiperbólica | β | A inclinação da curva |
| Gaussiana | σ | A largura do "sino" |
| Linear | k | A inclinação da reta |

**Funções parcialmente diferenciáveis** (têm pontos sem derivada):

| Função | Parâmetro que varia | O que ele muda |
|---|---|---|
| Degrau | limiar | O ponto onde a saída passa de 0 para 1 |
| Degrau bipolar | limiar | O ponto onde a saída passa de -1 para 1 |
| Rampa simétrica | a | O ponto onde a função para de crescer (saturação) |

## O que é gerado ao rodar

Quando o código termina, ele cria na mesma pasta:

- Uma imagem para cada função (`logistica.png`, `tanh.png`, `gaussiana.png`, `linear.png`, `degrau.png`, `degrau_bipolar.png` e `rampa_simetrica.png`).
- Uma imagem com todas as funções juntas (`todas_as_funcoes.png`).
- Uma janela com os gráficos abertos na tela.

## O que precisa ter instalado

- Python 3.9 ou mais novo
- As bibliotecas `numpy` (cálculos) e `matplotlib` (gráficos)

## Passo a passo para executar

### 1. Instalar o Python

Baixe no site [python.org](https://www.python.org/downloads/). No Windows, na hora de instalar, marque a opção **Add Python to PATH**. Se esquecer, o terminal não reconhece o comando `python`.

### 2. Colocar o arquivo em uma pasta

Crie uma pasta (por exemplo, `atividade_rna`) e coloque o `graficos.py` dentro dela.

### 3. Abrir o terminal na pasta

- **Windows:** abra a pasta no Explorador de Arquivos, clique na barra de endereço, digite `cmd` e aperte Enter.
- **Linux ou Mac:** abra o terminal e use o comando `cd` para entrar na pasta.

### 4. Criar o ambiente virtual (opcional)

Não é obrigatório, mas eu recomendo. O ambiente virtual deixa as bibliotecas desse projeto separadas das de outros projetos, o que evita conflito de versões.

No Windows:
```
python -m venv venv
venv\Scripts\activate
```

No Linux ou Mac:
```
python3 -m venv venv
source venv/bin/activate
```

Se der certo, vai aparecer `(venv)` no começo da linha do terminal.

### 5. Instalar as bibliotecas

```
pip install numpy matplotlib
```

### 6. Rodar o código

```
python graficos.py
```

No Windows, se o `python` não funcionar, tente `py graficos.py`. No Linux ou Mac, use `python3 graficos.py`.

Pronto! As imagens vão aparecer na pasta e uma janela com os gráficos vai abrir.

## Outra opção: Google Colab

Se você não quiser instalar nada no computador, dá para rodar online:

1. Entre em [colab.research.google.com](https://colab.research.google.com) e crie um novo notebook.
2. Copie o conteúdo do `graficos.py`, cole em uma célula e execute.
3. Os gráficos aparecem logo abaixo da célula, e as imagens ficam no painel de arquivos, do lado esquerdo.

## Como testar outros valores

No `graficos.py` tem uma lista chamada `graficos`. Em cada linha, os números entre colchetes são os valores que serão testados. Por exemplo:

```python
("Logística (β)", "logistica.png", logistica, [0.5, 1, 3]),
```

Se quiser testar outros valores de β, basta trocar `[0.5, 1, 3]` pelos números que preferir e rodar o código de novo.

## Erros comuns e como resolver

| Erro | O que significa e o que fazer |
|---|---|
| `ModuleNotFoundError: No module named 'numpy'` | As bibliotecas não estão instaladas onde você está rodando. Refaça o passo 5 (se estiver usando o `venv`, confira se ele está ativado). |
| `python não é reconhecido` | O Python não foi adicionado ao PATH. Use `py graficos.py` ou reinstale o Python marcando **Add Python to PATH**. |
| Erro ao ativar o `venv` no PowerShell | O Windows bloqueou o script. Use o Prompt de Comando (cmd) ou rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` no PowerShell. |
| O terminal fica "travado" no final | A janela do gráfico ainda está aberta. Feche ela e o código termina. |
