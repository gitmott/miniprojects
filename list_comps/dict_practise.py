# passed_students = {new_key:new_value for (student, score) in student_scores.item() if score > 50}


# sentence = "What is the airspeed velocity of an unladen swallow?"

# split_sentence = sentence.split(" ")
# result = {word:len(word) for word in split_sentence}

# print(result)

# weather_celcius = {"Monday": 12, "Tuesday": 17, "Wednesday": 21, "Thursday": 26, "Friday": 23}
# weather_fahrenheit = {day:(temp*9/5 + 32) for (day, temp) in weather_celcius.items()}
# print(weather_fahrenheit)

import pandas
student_dict = {
    "student": ["Matt", "Egg", "Fred"],
    "score": [100, 12, 69]
}

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(key, value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Egg":
        print(row.score)


