def main():
    while True:
        direction = input("Would you like to convert with Kg and Cm or lb and In? ").strip().lower()

        if direction in ("kg and cm", "kg & cm", "kilograms and centimeters", "kilograms & centimeters", "metric"):
            weight_kg = float(input("Enter your weight in kilograms: "))
            height_cm = float(input("Enter your height in centimeters: "))
            height_m = height_cm / 100  # Convert cm to meters
            bmi = weight_kg / (height_m ** 2)
            print(f"Your BMI is: {bmi:.2f}")

        elif direction in ("lb and in", "lb & in", "pounds and inches", "pounds & inches", "imperial", "pounds", "inches"):
            weight_lb = float(input("Enter your weight in pounds: "))
            height_in = float(input("Enter your height in inches: "))
            bmi = (weight_lb / (height_in ** 2)) * 703
            print(f"Your BMI is: {bmi:.2f}")

        else:
            print("Invalid option. Please try again.")
            continue

        # BMI categories
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")

        answer = input("Thank you for using the BMI calculator, would you like to calculate again? (y/n) ").strip().lower()
        if answer not in ("y", "yes", "sure", "yeah", "ok", "okay"):
            print("Have a nice day!")
            break

main()