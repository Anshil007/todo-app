import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        key_name = f"todo_{index}"
        if key_name in st.session_state:
            del st.session_state[key_name]
        st.rerun()

st.text_input(
    label="",
    placeholder="Add a new todo...",
    on_change=add_todo,
    key="new_todo")