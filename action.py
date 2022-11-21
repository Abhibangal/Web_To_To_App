import functions


def add(action, filepath):
    if action != '' and filepath != '':
        action = action.strip('\n')
        todo = action.title() + "\n"
        todos = functions.read_write_file(filepath, 'r')
        todos.append(todo)
        functions.read_write_file(filepath, 'w', todos)


def show(filepath):
    todos = functions.read_write_file(filepath, 'r')
    return todos
    #
    # for ind, item in enumerate(todos):
    #     item = item.strip('\n')
    #     print((f"{ind + 1}- {item}"))

        # f string to remove the space in between


def edit(existing_val, new_val, filepath):
    todos = functions.read_write_file(filepath, 'r')
    ind = todos.index(existing_val + '\n')
    todos[ind] = new_val.title() + '\n'

    functions.read_write_file(filepath, 'w', todos)


def complete(remove_val, filepath):
    todos = functions.read_write_file(filepath, 'r')
    num = todos.index(remove_val)
    print(num)
    todos.pop(num)
    functions.read_write_file(filepath, 'w', todos)


def clear(filepath):
    todos = functions.read_write_file(filepath, 'r')
    todos.clear()
    functions.read_write_file(filepath, 'w', todos)

