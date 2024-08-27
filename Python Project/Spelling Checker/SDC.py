from tkinter import *
from textblob import TextBlob
import requests

root = Tk()
root.title("Spelling & Dictionary Checker")
root.geometry("800x500")
root.config(background="#1c1c1c")


# Function to fetch the meaning and an example sentence
def get_meaning_and_example(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]['meanings'][0]['definitions'][0].get('definition', 'No definition found.')
        example = data[0]['meanings'][0]['definitions'][0].get('example', 'No example available.')
        return meanings, example
    return "No definition found.", "No example available."


# Function to check the spelling and provide the meaning and example
def check_spelling():
    word = enter_text.get()
    corrected_word = str(TextBlob(word).correct())

    meaning, example = get_meaning_and_example(corrected_word)

    spell_label.config(text=f"Corrected Word: {corrected_word}")
    meaning_label.config(text=f"Meaning: {meaning}")
    example_label.config(text=f"Example: {example}")


# Heading of the Application
heading = Label(root, text="Spelling & Dictionary Checker", font=("Helvetica", 35, "bold"), bg="#1c1c1c", fg="#ffd700")
heading.pack(pady=(30, 10))

# Entry widget to enter the text
enter_text = Entry(root, justify="center", width=30, font=("Helvetica", 25), bg="#ffffff", fg="#333333", border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Button to trigger the check_spelling function
button = Button(root, text="Check", font=("Helvetica", 20, "bold"), fg="#ffffff", bg="#ff4500",
                activebackground="#ff6347", activeforeground="#ffffff", command=check_spelling)
button.pack(pady=10)

# Labels to display the corrected word, meaning, and example
spell_label = Label(root, font=("Helvetica", 22, "bold"), bg="#1c1c1c", fg="#ffd700", wraplength=600, justify="left")
spell_label.pack(pady=20)

meaning_label = Label(root, font=("Helvetica", 18), bg="#1c1c1c", fg="#f5f5f5", wraplength=600, justify="left")
meaning_label.pack(pady=10)

example_label = Label(root, font=("Helvetica", 18, "italic"), bg="#1c1c1c", fg="#87ceeb", wraplength=600,
                      justify="left")
example_label.pack(pady=10)

root.mainloop()