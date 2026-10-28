import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 500)

# Funções de ativação
logistica = lambda x, b=1: 1 / (1 + np.exp(-b * x))
tanh      = lambda x, b=1: np.tanh(b * x)
gauss     = lambda x, s=1, c=0: np.exp(-(x - c) ** 2 / (2 * s ** 2))
linear    = lambda x, k=1: k * x
degrau    = lambda x, t=0: (x >= t).astype(float)
bipolar   = lambda x, t=0: np.where(x >= t, 1.0, -1.0)
rampa     = lambda x, a=1: np.clip(x, -a, a)

# (título, arquivo, função, valores do parâmetro)
graficos = [
    ("Logística (β)", "logistica.png", logistica, [0.5, 1, 3]),
    ("Tangente hiperbólica (β)", "tanh.png", tanh, [0.5, 1, 3]),
    ("Gaussiana (σ)", "gaussiana.png", gauss, [0.5, 1, 2]),
    ("Linear (k)", "linear.png", linear, [0.5, 1, 2]),
    ("Degrau (limiar)", "degrau.png", degrau, [-2, 0, 2]),
    ("Degrau bipolar (limiar)", "degrau_bipolar.png", bipolar, [-2, 0, 2]),
    ("Rampa simétrica (a)", "rampa_simetrica.png", rampa, [1, 2, 4]),
]

# 1) Um arquivo PNG por função
for titulo, arquivo, f, params in graficos:
    plt.figure(figsize=(5, 4))
    for p in params:
        plt.plot(x, f(x, p), label=str(p))
    plt.title(titulo)
    plt.grid(True)
    plt.legend()
    plt.savefig(arquivo, dpi=150)
    plt.close()

# 2) Imagem com todas as funções juntas
fig, axs = plt.subplots(3, 3, figsize=(12, 9))
for ax, (titulo, _, f, params) in zip(axs.flat, graficos):
    for p in params:
        ax.plot(x, f(x, p), label=str(p))
    ax.set_title(titulo)
    ax.grid(True)
    ax.legend()
for ax in axs.flat[len(graficos):]:
    ax.axis("off")
plt.tight_layout()
plt.savefig("todas_as_funcoes.png", dpi=150)
plt.show()