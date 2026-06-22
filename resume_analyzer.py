def analyze_resume(text):

    required_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Statistics",
        "HTML",
        "CSS",
        "JavaScript"
    ]

    detected_skills = []

    for skill in required_skills:

        if skill.lower() in text.lower():
            detected_skills.append(skill)

    score = int(
        (len(detected_skills) / len(required_skills))
        * 100
    )

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in detected_skills
    ]

    return detected_skills, score, missing_skills