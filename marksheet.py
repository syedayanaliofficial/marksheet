import streamlit as st

subjects = ["Computer", "Physics", "Chemistry", "English", "Urdu"]
max_marks = 100


def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"


st.title("Marksheet")
name = st.text_input("Student Name")
roll_no = st.text_input("Roll No")

marks_list = []
for subject in subjects:
    marks = st.number_input(f"{subject} Marks", min_value=0.0, max_value=100.0, step=0.5)
    marks_list.append(marks)

if st.button("Generate Marksheet"):
    rows = []
    percent_sum = 0
    for i in range(len(subjects)):
        percentage = marks_list[i] / max_marks * 100
        percent_sum += percentage
        rows.append({
            "Subject": subjects[i],
            "Total": max_marks,
            "Obtained": marks_list[i],
            "Percentage": f"{percentage:.2f}%",
            "Grade": get_grade(percentage),
        })
    overall = percent_sum / len(subjects)
    st.write(f"**Name:** {name} | **Roll No:** {roll_no}")
    st.table(rows)
    st.write(f"**Overall Percentage:** {overall:.2f}%")
    st.write(f"**Overall Grade:** {get_grade(overall)}")