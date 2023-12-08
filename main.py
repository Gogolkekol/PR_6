# main.py
from python_module_practice6.app.Calculator import Calculator

def main():
    calculator_instance = Calculator(10, 2)

    result_addition = calculator_instance.addition()
    result_subtraction = calculator_instance.subtraction()
    result_multiplication = calculator_instance.multiplication()
    result_division = calculator_instance.division()
    result_power = calculator_instance.power()
    random_number = Calculator.random_number(1, 100)

    print(f"Addition: {result_addition}")
    print(f"Subtraction: {result_subtraction}")
    print(f"Multiplication: {result_multiplication}")
    print(f"Division: {result_division}")
    print(f"Power: {result_power}")
    print(f"Random Number: {random_number}")

if __name__ == "__main__":
    main()
