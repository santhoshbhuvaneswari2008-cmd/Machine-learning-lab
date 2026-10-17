"""Helper functions: validated input and risk category."""


def get_number(prompt, low, high):
    """Keep asking until a number between low and high is entered."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue
        if low <= value <= high:
            return value
        print(f"  Value must be between {low} and {high}. Try again.")


def get_category(probability):
    """Convert approval probability into a risk category."""
    if probability >= 0.75:
        return "Low Risk"
    if probability >= 0.50:
        return "Medium Risk"
    return "High Risk"
