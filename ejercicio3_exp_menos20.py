# Edison Ogonaga deber interpolación y polinomios de Taylor
import math


def taylor_exp(x, n=100):
    termino = 1.0
    suma = 1.0
    max_abs = 1.0
    for k in range(1, n + 1):
        termino = termino * x / k
        suma = suma + termino
        if abs(termino) > max_abs:
            max_abs = abs(termino)
    return suma, max_abs


if __name__ == "__main__":
    p100_menos20, max_termino = taylor_exp(-20.0, 100)
    valor_real = math.exp(-20.0)
    p100_mas20, _ = taylor_exp(20.0, 100)
    inverso_p100 = 1.0 / p100_mas20

    print(f"Valor real math.exp(-20):       {valor_real:.10e}")
    print(f"Suma directa P_100(-20):        {p100_menos20:.10e}")
    print(f"Mayor valor absoluto |(-20)^k/k!|: {max_termino:.6f} ({max_termino:.6e})")
    print(f"1 / P_100(20):                  {inverso_p100:.10e}")
