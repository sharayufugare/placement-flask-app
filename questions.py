import random

APTITUDE_QUESTIONS = [
    ("10 + 15 = ?", ["20", "25", "30"], "25"),
    ("5 × 8 = ?", ["30", "40", "45"], "40"),
    ("100 / 5 = ?", ["20", "25", "30"], "20"),
    ("2, 4, 8, ?", ["12", "14", "16"], "16"),
    ("Square root of 81?", ["7", "8", "9"], "9")
]

SOFT_SKILL_QUESTIONS = [
    ("Good communication means?", ["Clear expression", "Fast talking"], "Clear expression"),
    ("Teamwork needs?", ["Cooperation", "Competition"], "Cooperation"),
    ("Leadership quality?", ["Guiding team", "Ordering"], "Guiding team"),
    ("Conflict handling?", ["Ignore", "Solve calmly"], "Solve calmly"),
    ("Professional behavior?", ["Responsibility", "Carelessness"], "Responsibility")
]

def get_random_questions(question_list, count=3):
    return random.sample(question_list, count)
