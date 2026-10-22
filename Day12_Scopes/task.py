def is_prime(num):
    for i in range(2, num ):
        print(f"val i: {i}")
        if num % i == 0:
            return False
    return True

print(f"is_prime: {is_prime(10)}")