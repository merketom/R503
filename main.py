import random

# -------- Exponentiation modulaire --------
def exp_modulaire(a, b, n):
    result = 1
    a = a % n
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        b //= 2
    return result

# -------- Test de Fermat --------
def test_fermat(N, k=5):
    """Teste si N est premier avec le test de Fermat (probabiliste).
       k = nombre de bases aléatoires testées."""
    if N <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, N - 2)
        if exp_modulaire(a, N - 1, N) != 1:
            return False  # N est composé
    return True  # N est probablement premier

# -------- Tirage d'un grand nombre premier --------
def tirer_premier(min_val=10**6, max_val=10**9):
    while True:
        N = random.randint(min_val, max_val)
        if test_fermat(N, k=10):  # plus k est grand, plus on a confiance
            return N

# -------- Exemple d'utilisation --------
p = tirer_premier()
q = tirer_premier()
print("p =", p)
print("q =", q)
