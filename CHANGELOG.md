# Changelog

## 1.1

- M-01 (`solution_type.py` / `get_solution_type`): la clasificación del sistema
  ahora usa el teorema de Rouché–Frobenius con rangos exactos (SymPy) en lugar
  del determinante flotante con tolerancia `1e-3` y la revisión del último
  renglón de la RREF. Corrige los hallazgos H-01 y H-02.
- M-02 (`solution_type.py` / `interpret_rref`): se corrigió la construcción de
  la expresión paramétrica de las soluciones infinitas (antes insertaba el valor
  de la columna siguiente y dejaba impresiones de depuración). Corrige el
  hallazgo H-03.

## 1.0

- Versión original recibida (`main.py`, `solution_type.py`).
