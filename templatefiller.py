# Define the template
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Function to fill the template
def fill_letter(name, date):
    filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)
    return filled_letter

# Example usage
name = input('enter your name: ')#"Kelvin"
date = input("enter date: ")#"2nd August 2026"
print(fill_letter(name, date))
