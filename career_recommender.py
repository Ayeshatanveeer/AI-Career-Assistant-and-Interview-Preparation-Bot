import json

with open("career_data.json", "r") as file:
    careers = json.load(file)

def recommend_career(user_skills):

    best_match = None
    max_score = 0

    for career, details in careers.items():

        score = len(
            set(user_skills).intersection(
                set(details["skills"])
            )
        )

        if score > max_score:
            max_score = score
            best_match = career

    return best_match