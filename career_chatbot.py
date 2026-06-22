import json

with open("career_data.json", "r") as file:
    data = json.load(file)

def chatbot_response(user_input):

    user_input = user_input.lower()

    if "data scientist" in user_input:

        return """
Career: Data Scientist

Skills:
- Python
- SQL
- Machine Learning
- Statistics

Roadmap:
1. Learn Python
2. Learn SQL
3. Learn Statistics
4. Learn Machine Learning
5. Build Projects
"""

    elif "web developer" in user_input:

        return """
Career: Web Developer

Skills:
- HTML
- CSS
- JavaScript
- Python

Roadmap:
1. Learn HTML
2. Learn CSS
3. Learn JavaScript
4. Learn Flask
"""

    else:

        return "Sorry, I don't have information about that career."