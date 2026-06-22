import streamlit as st
import json

from career_recommender import recommend_career
from interview_bot import get_questions
from resume_analyzer import analyze_resume
from career_chatbot import chatbot_response
# Load career data
with open("career_data.json", "r") as file:
    career_data = json.load(file)

st.title("AI Career Assistant")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Career Recommendation",
        "Interview Preparation",
        "Resume Analyzer",
        "Career Chatbot"
    ]
)

# ---------------------------
# Career Recommendation
# ---------------------------
if menu == "Career Recommendation":

    skills = st.text_input(
        "Enter your skills separated by comma"
    )

    if st.button("Recommend"):

        user_skills = [
            s.strip()
            for s in skills.split(",")
        ]

        career = recommend_career(user_skills)

        st.success(
            f"Recommended Career: {career}"
        )

        # Show Roadmap
        if career in career_data:

            st.subheader("Learning Roadmap")

            for step in career_data[career]["roadmap"]:
                st.write("📌", step)

            st.subheader("Required Skills")

            for skill in career_data[career]["skills"]:
                st.write("✅", skill)

# ---------------------------
# Interview Preparation
# ---------------------------
elif menu == "Interview Preparation":

    career = st.selectbox(
        "Select Career",
        [
            "Data Scientist",
            "Web Developer"
        ]
    )

    if st.button("Start Interview"):

        questions = get_questions(career)

        st.subheader("Interview Questions")

        for q in questions:
            st.write("❓", q)

# ---------------------------
# Resume Analyzer
# ---------------------------
elif menu == "Resume Analyzer":

    resume = st.text_area(
        "Paste Resume Text"
    )

    if st.button("Analyze"):

        detected_skills, score, missing_skills = analyze_resume(resume)

        st.subheader("Resume Score")

        st.success(f"{score}/100")

        st.subheader("Detected Skills")

        for skill in detected_skills:
            st.write("✅", skill)

        st.subheader("Missing Skills")

        for skill in missing_skills:
            st.write("❌", skill)


elif menu == "Career Chatbot":

    st.subheader("Career Chatbot")

    user_query = st.text_input(
        "Ask about a career"
    )

    if st.button("Ask"):

        response = chatbot_response(
            user_query
        )

        st.write(response)