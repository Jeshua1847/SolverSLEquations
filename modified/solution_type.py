import numpy as np
from sympy import Matrix, pprint, nsimplify


# from solution_infinite import interpret_rref
def interpret_rref(rref_matrix):
    num_rows, num_cols = rref_matrix.shape
    solutions = []
    free_vars_positions = set(range(num_cols - 1))  # Excluding the constant column

    # Identify pivot variables and remove them from the free_vars_positions set
    for i in range(num_rows):
        row = rref_matrix[i, :]
        leading_entry_index = next((index for index, val in enumerate(row) if val != 0), None)
        if leading_entry_index is not None:  # If there's a leading entry
            free_vars_positions.discard(leading_entry_index)

    # Express solution in terms of free variables
    for i in range(num_rows):
        row = rref_matrix[i, :]
        leading_entry_index = next((index for index, val in enumerate(row) if val != 0), None)

        if leading_entry_index is None:  # All zero row
            continue

        # A leading entry in the constant column means an inconsistent row;
        # it must never be treated as a variable equation.
        if leading_entry_index == num_cols - 1:
            continue

        # Construct the expression for the leading variable in terms of free variables
        terms = []
        for j in sorted(free_vars_positions):
            if row[j] != 0:
                terms.append(f"{-row[j]}x{j + 1}")
        if row[-1] != 0:
            terms.append(str(row[-1]))
        if terms:
            expression = f"x{leading_entry_index + 1} = " + " + ".join(terms)
        else:
            expression = f"x{leading_entry_index + 1} = 0"
        solutions.append(expression)

    for free_var_pos in sorted(free_vars_positions):
        solutions.append(f"x{free_var_pos + 1} is a free variable")
    print(solutions)

    return solutions


def get_solution_type(a_mat, b):
    det_a = np.linalg.det(a_mat)
    # Print the determinant of the matrix A (informational only)
    print("The determinant of the matrix A is : ", det_a)

    augmented_a = Matrix(np.column_stack((a_mat, b)))
    # To rationalize the augmented matrix (solves the floating point precision problem
    augmented_a = augmented_a.applyfunc(lambda x: nsimplify(x, rational=True))

    # Print the augmented matrix
    print("The augmented matrix is: ")
    pprint(augmented_a)

    rref_matrix = augmented_a.rref()[0]

    # Print the reduced row echelon form of the augmented matrix
    print("The reduced row echelon form of the augmented matrix is: ")
    pprint(rref_matrix)

    # Exact classification with the Rouché-Frobenius theorem:
    # compare the rank of the coefficient matrix with the rank of the
    # augmented matrix, using exact rational arithmetic (no float tolerance).
    coeff_a = augmented_a[:, :-1]
    rank_a = coeff_a.rank()
    rank_aug = augmented_a.rank()
    num_unknowns = coeff_a.shape[1]

    if rank_a < rank_aug:
        return "The system has no solution."
    elif rank_a == num_unknowns:
        # Unique solution: for a square nonsingular system the RREF of the
        # augmented matrix is [I | x], so the solution is its last column.
        solution = rref_matrix[:, -1]
        return f"The system has a unique solution: {list(solution)}"
    else:
        interpret_rref(rref_matrix)
        return "The system has infinitely many solutions."


def input_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = float(input(f"Enter the value for row {i + 1}, column {j + 1}: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        matrix.append(row)
    return np.array(matrix)


def input_vector(length):
    vector = []
    for i in range(length):
        while True:
            try:
                value = float(input(f"Enter the value for element {i + 1} of the vector  b: "))
                vector.append(value)
                break
            except ValueError:
                print("Please enter a valid number.")
    return np.array(vector)
