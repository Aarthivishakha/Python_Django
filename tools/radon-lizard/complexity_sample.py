"""Cyclomatic complexity fixture for radon / lizard."""


def grade_student(score, is_bonus, is_premium, attendance):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    if is_bonus and score < 100:
        grade += "+"
    if is_premium and attendance >= 0.9:
        grade += " (honors)"
    elif is_premium and attendance < 0.5:
        grade += " (probation)"

    if attendance < 0.75 and not is_premium:
        grade += " (attendance-warning)"

    return grade
