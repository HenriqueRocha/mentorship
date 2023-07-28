#file_path = "names.txt"

'''with open(file_path, 'r') as file:
    for line in file:
        print("**" + line.strip().upper() + "**")'''

# The file will be automatically closed after the 'with' block
# appending file(adding text at end of  file)
def append_text_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write('\n' + text)

# Example usage
file_path = 'names.txt'
text_to_append = 'Tina.'

append_text_to_file(file_path, text_to_append)


