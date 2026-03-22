FILEPATH = 'files/todos.txt'

def get_todos(filepath=FILEPATH):
	with open(filepath, 'r') as file:
		todos_retrieved = file.readlines()
	return todos_retrieved


def write_todos(todos_arg,filepath=FILEPATH):
	with open(filepath, 'w') as file:
		file.writelines(todos_arg)

print(__name__)
if __name__ == '__main__':
	FILEPATH = '../files/todos.txt'
	print(FILEPATH)
	print('Hello from Functions')
	print(get_todos(FILEPATH))