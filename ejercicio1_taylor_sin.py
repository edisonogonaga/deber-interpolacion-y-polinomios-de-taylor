# Edison Ogonaga deber interpolación y polinomios de Taylor
import numpy as np
import matplotlib.pyplot as plt


def taylor_sin(x, n):
    termino = x
    suma = x * 1.0
    max_k = (n - 1) // 2
    for k in range(max_k):
        termino = termino * (-x**2) / ((2 * k + 2) * (2 * k + 3))
        suma = suma + termino
    return suma


if __name__ == "__main__":
    p9_pi = taylor_sin(np.pi, 9)
    print(f"1. P_9(pi) = {p9_pi:.10f} (con 6 decimales: {p9_pi:.6f})")

    x_g1 = np.linspace(-2 * np.pi, 2 * np.pi, 600)
    plt.figure(figsize=(9, 6))
    plt.plot(x_g1, np.sin(x_g1), "k-", linewidth=2.5, label=r"$\sin x$")

    grados_g1 = [1, 3, 5, 7, 9]
    for g in grados_g1:
        plt.plot(x_g1, taylor_sin(x_g1, g), "--", linewidth=1.6, label=f"$P_{{{g}}}(x)$ (grado {g})")

    plt.axhline(0, color="gray", linewidth=0.8, linestyle=":")
    plt.ylim(-2, 2)
    plt.xlim(-2 * np.pi, 2 * np.pi)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.title(r"Gráfica 1: $\sin x$ y polinomios de Maclaurin $P_1, P_3, P_5, P_7, P_9$ en $[-2\pi, 2\pi]$", fontsize=13)
    plt.legend(loc="upper right")
    plt.grid(True, alpha=0.35)
    plt.tight_layout()
    plt.savefig("grafica1_taylor_sin.png", dpi=150)

    grados = list(range(1, 22, 2))
    x_pi = np.linspace(-np.pi, np.pi, 2001)
    x_pi4 = np.linspace(-np.pi / 4, np.pi / 4, 2001)

    err_pi = []
    err_pi4 = []

    print("\nGrado n | Error máx en [-pi, pi] | Error máx en [-pi/4, pi/4]")
    for n in grados:
        e1 = np.max(np.abs(np.sin(x_pi) - taylor_sin(x_pi, n)))
        e2 = np.max(np.abs(np.sin(x_pi4) - taylor_sin(x_pi4, n)))
        err_pi.append(e1)
        err_pi4.append(e2)
        print(f"  n={n:2d}  |      {e1:.6e}      |        {e2:.6e}")

    menor_n_pi = next(n for n, e in zip(grados, err_pi) if e < 1e-8)
    menor_n_pi4 = next(n for n, e in zip(grados, err_pi4) if e < 1e-8)
    print(f"\n2. Menor grado impar con error < 10^-8 en [-pi, pi]:     {menor_n_pi}")
    print(f"   Menor grado impar con error < 10^-8 en [-pi/4, pi/4]: {menor_n_pi4}")

    plt.figure(figsize=(9, 6))
    plt.semilogy(grados, err_pi, "o-", color="crimson", linewidth=2, markersize=6,
                 label=r"Error máximo en $[-\pi, \pi]$")
    plt.semilogy(grados, err_pi4, "s-", color="steelblue", linewidth=2, markersize=6,
                 label=r"Error máximo en $[-\pi/4, \pi/4]$")
    plt.axhline(1e-8, color="black", linestyle="--", linewidth=1.2, label=r"Tolerancia $10^{-8}$")

    plt.xticks(grados)
    plt.xlabel("Grado impar n", fontsize=12)
    plt.ylabel(r"Error máximo $\max|\sin x - P_n(x)|$", fontsize=12)
    plt.title(r"Gráfica 2: Error máximo de Taylor de $\sin x$ frente al grado $n$", fontsize=13)
    plt.legend(loc="upper right")
    plt.grid(True, which="both", alpha=0.35)
    plt.tight_layout()
    plt.savefig("grafica2_error_taylor_sin.png", dpi=150)
