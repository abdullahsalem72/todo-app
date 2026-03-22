from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b - %d - %Y, %H:%M:%S ")
print(f"The time is: {now}")
todos = get_todos()

while True:  # Or While True and create break at case
	user_input = input('Show or Add or Edit or Done ?')
	user_input = user_input.strip().lower()

	if user_input.startswith('show'):
		# with open('todos.txt', 'r') as file:
		# todos = file.read().splitlines()
		# file = open('files/todos.txt', 'r')
		# todos =  file.read().splitlines()
		# todos= file.readlines()
		# file.close()

		# better method than file open and close
		# with open('files/todos.txt', 'r') as file:
		# 	todos = file.readlines()

		todos = get_todos()

		# new_todos= []
		# for item in todos:
		# new_item = item.strip('\n')
		# new_todos.append(new_item)

		# new_todos = [item.strip('\n') for item in todos	]#Shorter version compared to above 4 lines
		for index, item in enumerate(todos):
			item = item.strip('\n').title()  # more simplere than inline 4 for loop above
			# print(f"{index}: {item}")
			row = f"{index + 1}-{item}"
			print(row)
		print(f"The length is {index} and last entry is {item}")
		print(f"The Sorted is {sorted(todos)}")



	elif user_input.startswith('add'):

		todo = user_input[4:]
		todos = get_todos()
		todos.append(todo + '\n')

		write_todos(todos)


	elif user_input.startswith('edit'):

		try:
			todo_position = int(user_input[5])

			todos = get_todos()
			todo = todos[todo_position - 1]
			todos[todo_position - 1] = input('Enter Revised Todo..') + '\n'

			write_todos(todos)

		except ValueError:
			print('Wrong Command Sequence !!!')
			continue

		except IndexError:
			print('Out of Range !!!')
			continue


	elif user_input.startswith('done'):

		try:
			todo = int(user_input[5])

			todos = get_todos()

			todos.pop(todo - 1)

			write_todos(todos)


		except IndexError:
			print('Out of Range !!! / Wrong Position Entered')
			continue

		except ValueError:
			print('Wrong Command Sequence !!!')
			continue

	# if 0 <= todo <= len(todos):
	#
	# 	todos.pop(todo - 1)
	#
	# 	with open('files/todos.txt', 'w') as file:
	#
	# 		file.writelines(todos)
	#
	# else:
	# 	print('Out of Range !!!')

	elif user_input.startswith('done'):

		print('Goodbye!')

		break

	else:

		print('Invalid Input!!!')

print('Bye...')
