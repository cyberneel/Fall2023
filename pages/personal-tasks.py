import streamlit as st

st.title("To-Do List")

# Input field for adding tasks
task = st.text_input("Add a task")

# Initialize session state to store tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Button to add a task
if st.button("Add Task"):
    if task:
        st.session_state.tasks.append({"task": task, "completed": False})
        task = ""

# Checkbox to mark all tasks as completed
if st.checkbox("Mark All"):
    for t in st.session_state.tasks:
        t["completed"] = True

# Checkbox to show completed tasks
show_completed = st.checkbox("Show Completed Tasks")
if show_completed:
    tasks_to_display = st.session_state.tasks
else:
    tasks_to_display = [t for t in st.session_state.tasks if not t["completed"]]

# Display the list of tasks with checkboxes
st.write("### Tasks")
if tasks_to_display:
    for i, t in enumerate(tasks_to_display, start=1):
        task = t["task"]
        completed = t["completed"]
        t["completed"] = st.checkbox(f"{i}. {task}", value=completed)
else:
    st.write("No tasks added")

# Button to clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]

# Button to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []