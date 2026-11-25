# SolverSLEquations

Programa interactivo en Python que clasifica y resuelve sistemas de ecuaciones
lineales (SEL) cuadrados \(Ax = b\). Para cada sistema imprime el determinante,
la matriz aumentada, su forma escalonada reducida por renglones (RREF) y la
clasificación del sistema: solución única, infinitas soluciones o sin solución.

## Requisitos

- Python 3
- NumPy
- SymPy

Instalación de dependencias:

```bash
pip install numpy sympy
```

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

El programa pide:

1. El tamaño `m` de la matriz cuadrada.
2. Los `m × m` valores de la matriz `A`, renglón por renglón.
3. Los `m` valores del vector `b`.

Al final pregunta si se desea capturar otro sistema.

## Ejemplo

Para el sistema \(2x + y = 5\), \(x - y = 1\) (matriz `[[2, 1], [1, -1]]`,
vector `[5, 1]`), la salida termina con:

```
The system has a unique solution: [2, 1]
```

## Criterio de clasificación

La clasificación usa el teorema de Rouché–Frobenius con aritmética racional
exacta (SymPy), comparando el rango de `A` con el rango de la matriz aumentada
`[A|b]`:

- `rango(A) < rango(A|b)`: el sistema no tiene solución.
- `rango(A) = n` (número de incógnitas): solución única, leída de la RREF.
- En otro caso: infinitas soluciones, expresadas en forma paramétrica.

## Archivos

- `main.py`: menú interactivo de captura.
- `solution_type.py`: clasificación y resolución (`get_solution_type`,
  `interpret_rref`).
