#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from pathlib import Path

Names = []
def copy_content():
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter_blueprint:
        content = letter_blueprint.read()
        return content

def get_input_names():
    global Names
    path = Path(r".\Input\Names\invited_names.txt")
    with open(path, mode="r") as names:
        Names = names.readlines()
        # for name in names:
        #     clean_name = name.strip()
        #     NAMES.append(clean_name)

get_input_names()

def send_mails():
    global Names
    output_dir = Path(r"Output/ReadyToSend")
    output_dir.mkdir(parents=True, exist_ok=True)
    for name in Names:
        clean_name = name.strip()
        file_dir = output_dir/ f"SendTo{clean_name}.docx"
        replacing_content = copy_content()
        replacing_content = replacing_content.replace("[name]", clean_name)
        with open(file_dir, mode="w") as file:
            file.write(replacing_content)

send_mails()





