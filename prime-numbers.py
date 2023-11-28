def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_prime():
    prime_numbers = [num for num in range(1, 251) if is_prime(num)]

    for prime_number in prime_numbers:
        print(prime_number)

    with open('results.txt', 'w') as file:
        for prime_number in prime_numbers:
            file.write(str(prime_number) + '\n')

if __name__ == "__main__":
    display_prime()
