UNIVERSAL_NAME = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as content:
    letter = content.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace(UNIVERSAL_NAME, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as output_letters:
            completed_letters = output_letters.write(new_letter)
