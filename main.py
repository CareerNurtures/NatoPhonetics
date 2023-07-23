

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index,row) in data.iterrows()}

text = input("Enter a text: ").upper()

list_data = [word for word in text if word.isalnum()]

final_list = [data_dict[word] for word in list_data]
print(final_list)




