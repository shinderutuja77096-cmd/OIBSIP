def get_float_input(prompt):
    while True:
        value = input(prompt)
        try:
            num = float(value)
            if num <= 0:
                print("Value must be greater than zero. Please try again.")
                continue
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== BMI Calculator ===")
    weight = get_float_input("Enter your weight in kg: ")
    height = get_float_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()