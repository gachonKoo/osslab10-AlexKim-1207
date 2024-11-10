def get_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Divisors of", number, "are:", get_divisors(number))
