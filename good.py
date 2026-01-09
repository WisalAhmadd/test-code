import subprocess
from typing import Optional


def add_numbers(a: int, b: int) -> int:
    return a + b


def calculate_value(x: int) -> str:
    return "Ten" if x == 10 else "Not ten"


def safe_divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def run_safe_command(command: list[str]) -> None:
    subprocess.run(command, check=True)


def sum_values(values: list[int]) -> int:
    return sum(values)


def main():
    print(add_numbers(5, 3))
    print(calculate_value(10))

    result = safe_divide(10, 2)
    if result is None:
        print("Cannot divide by zero")
    else:
        print(result)

    run_safe_command(["echo", "Hello SonarQube"])

    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(sum_values(numbers))


if __name__ == "__main__":
    main()
