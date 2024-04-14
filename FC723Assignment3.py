def euclidean_algorithm(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
def main():
    try:
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
        if a <= 0 or b <= 0:
            raise ValueError("Numbers must be positive integers.")
        result = euclidean_algorithm(a, b)
        print(f"The GCD of {a} and {b} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
