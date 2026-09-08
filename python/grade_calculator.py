def calculate_grade(score):
    if score < 0 or score > 100:
        return "Please enter a value between 0 and 100."
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

if __name__ == "__main__":
    try:
        score = float(input("Enter percentage score (0-100): "))
        print(f"Grade: {calculate_grade(score)}")
    except ValueError:
        print("Please enter a valid numeric value.")