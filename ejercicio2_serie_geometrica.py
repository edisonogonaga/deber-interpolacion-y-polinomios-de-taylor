# Edison Ogonaga deber interpolación y polinomios de Taylor
import numpy as np
import matplotlib.pyplot as plt


def serie_geometrica(x, N):
    termino = np.ones_like(x, dtype=float)
    suma = termino.copy()
    for _ in range(N):
        termino = termino * (-x**2)
        suma = suma + termino
    return suma


if __name__ == "__main__":
    s40_09 = float(serie_geometrica(0.9, 40))
    s40_11 = float(serie_geometrica(1.1, 40))
    print(f"S_40(0.9) = {s40_09:.10f}")
    print(f"S_40(1.1) = {s40_11:.6e} (exacto: {s40_11:.6f})")

    x = np.linspace(-1.5, 1.5, 600)
    f_exacta = 1.0 / (1.0 + x**2)

    plt.figure(figsize=(9, 6))
    plt.plot(x, f_exacta, "k-", linewidth=2.5, label=r"$\frac{1}{1+x^2}$")

    for N in [2, 5, 10, 20]:
        plt.plot(x, serie_geometrica(x, N), "--", linewidth=1.6, label=f"$S_{{{N}}}(x)$ (grado {2*N})")

    plt.axvline(-1.0, color="gray", linestyle=":", linewidth=1)
    plt.axvline(1.0, color="gray", linestyle=":", linewidth=1)
    plt.ylim(-0.5, 1.5)
    plt.xlim(-1.5, 1.5)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.title(r"Gráfica 3: $\frac{1}{1+x^2}$ y sumas parciales $S_N(x)$ para $N = 2, 5, 10, 20$ en $[-1.5, 1.5]$", fontsize=13)
    plt.legend(loc="upper center")
    plt.grid(True, alpha=0.35)
    plt.tight_layout()
    plt.savefig("grafica3_serie_geometrica.png", dpi=150)
