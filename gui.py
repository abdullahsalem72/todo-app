from unittest import case

import modules.functions
import FreeSimpleGUI as gui

from modules import functions

label = gui.Text("Type in a Todo..")
input_box = gui.InputText(tooltip="Enter To do", key='todo')
add_button = gui.Button("Add")

window = gui.Window('My To-Do App',
					layout=[[label], [input_box, add_button]],
					font=("Helvetica", 15))
while True:
	event, value = window.read()
	print(event)
	print(value)
	match event:
		case "Add":
			todos = functions.get_todos()
			new_todo = value['todo'] + '\n'
			todos.append(new_todo)
			functions.write_todos(todos)
			print(todos)

		case gui.WIN_CLOSED:
			break

window.close()
