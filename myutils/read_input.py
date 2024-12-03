
def read_problem_input(input_file):
    with open(input_file, 'r') as file:
        return file.read().strip().split('\n')

def read_problem_input_string(input_file):
    with open(input_file, 'r') as file:
        return file.read()
