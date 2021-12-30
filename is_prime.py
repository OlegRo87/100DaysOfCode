def prime_check(num):
    is_prime = True
    for i in range(2, num):
        if num % i== 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print ("It's not a prime number.")




prime_check(11)
