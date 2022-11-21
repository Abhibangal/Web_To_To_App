import streamlit as st
import action


todos = action.show('todos.txt')


def add_todo():
    n_todo = st.session_state["new_todo"]
    # print(ntodo)
    action.add(n_todo, 'todos.txt')


st.title('To Do App')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        action.complete(todo, 'todos.txt')
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter to do', placeholder='Add to do . . .', on_change=add_todo, key='new_todo')