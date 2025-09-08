import random

# --- Exponentiation modulaire ---
def exp_modulaire(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b //= 2
    return result

# --- Fermat ---
def test_fermat(N, k=5):
    if N <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, N - 2)
        if exp_modulaire(a, N - 1, N) != 1:
            return False
    return True

# --- Tirage grand nombre premier ---
def tirer_premier(min_val=10**6, max_val=10**9):
    while True:
        N = random.randint(min_val, max_val)
        if test_fermat(N, k=10):
            return N

# --- Exemple d'utilisation ---
p = tirer_premier()
q = tirer_premier()
print("p =", p)
print("q =", q)
