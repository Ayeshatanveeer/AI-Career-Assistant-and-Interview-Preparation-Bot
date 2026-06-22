import json

with open("career_data.json", "r") as file:
    careers = json.load(file)

def get_questions(career):

    if career in careers:
        return careers[career]["interview_questions"]

    return []