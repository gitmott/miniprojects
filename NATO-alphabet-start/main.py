import pandas

data = pandas.read_csv(r"C:\Users\Matt\repos\miniprojects\NATO-alphabet-start\nato_phonetic_alphabet.csv")
raw_df = pandas.DataFrame(data)
data_dict = {row.letter:row.code for (index, row) in raw_df.iterrows()}
word = input("Enter a word: ").upper()
nato_dict = [data_dict[letter] for letter in word]
print(nato_dict)