import pandas

data = pandas.read_csv(r"C:\Users\Matt\repos\miniprojects\password_manager\nato_phonetic_alphabet.csv")
raw_df = pandas.DataFrame(data)

data_dict = {row.letter:row.code for (index, row) in raw_df.iterrows()}


def generate():
    word = input("Enter a word: ").upper()
    try:
        nato_dict = [data_dict[letter] for letter in word]
    except KeyError:
        print("Wrong data type. Try again.")
        generate()
    else:
        print(nato_dict)

generate()