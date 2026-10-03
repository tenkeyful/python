def Sieve_of_Eratosthenes(lim):
    boolean_array = [True] * (lim + 1)
    boolean_array[0] = boolean_array[1] = False

    for k in range(2, int(lim**0.5) + 1):
        if boolean_array[k]:
          for m in range(k * k, lim + 1, k):
            boolean_array[m] = False

    return [n for n, is_prime_n in enumerate(boolean_array) if is_prime_n]

limit = 100
primes = Sieve_of_Eratosthenes(limit)
print(primes)

def Trial_Division(n):
    factors = []
    i = 2
    while n > 1:
      if n % i == 0:
        factors.append(i)
        n //= i
      else:
        i += 1
    return factors

n = 10
factors = Trial_Division(n)
print(f"Prime factors of {n}: {factors}")