def is_divisible(dividend, divisor):
    if dividend % divisor is 0:
        return True
    return False


if __name__ == "__main__":
    while True:
        value = input("\nEnter a value: ")
        try:
            value = int(value)
            if value < 1:
                raise ValueError
        except ValueError:
            print("Incorrect value. Please set int value >= 1.")
            continue

        for i in range(value, 0, -1):
            if is_divisible(i, 3) and is_divisible(i, 5):
                print("Testing")
                continue
            if is_divisible(i, 3):
                print("Software")
                continue
            if is_divisible(i, 5):
                print("Agile")
                continue
            print(i)
