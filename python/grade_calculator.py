"""Convert percentage scores into letter grades."""


def calculate_grade(score: float) -> str:
    """Return the letter grade for a score from 0 through 100."""
    if score < 0 or score > 100:
        return "Please enter a value between 0 and 100."
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "D"

if __name__ == "__main__":
    try:
        score = float(input("Enter percentage score (0-100): "))
        print(f"Grade: {calculate_grade(score)}")
    except ValueError:
        print("Please enter a valid numeric value.")