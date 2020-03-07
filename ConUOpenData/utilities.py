import csv
import json


UNHANDLED_CHARACTERS_AND_ESCAPES = ["\'", "\"", "\t", "\n"]
programs = []

index_to_value_mapping = {
    0: "course_id",
    1: "subject",
    2: "catalog",
    3: "title",
    4: "credits",
    5: "component",
    7: "pre-requisites",
    8: "career",
    9: "equivalencies"
}


def parse_csv_create_json():
    json_for_classes = open("classes_parsed.json", "w")
    json_for_classes.write("[")

    with open("Classes_catalog.csv") as classes_file:
        reader = csv.reader(classes_file)
        for row in reader:
            class_dict = {"class": {
            }}
            for index in index_to_value_mapping:
                row[index] = remove_unhandled_characters(row[index])

                class_dict['class'][index_to_value_mapping[index]] = row[index]

            print(class_dict)
            json_for_classes.write(str(class_dict).replace('\'', '\"'))
            json_for_classes.write(",")

        json_for_classes.write("]")
        print("done")


def remove_unhandled_characters(given_string):
    for character in UNHANDLED_CHARACTERS_AND_ESCAPES:
        if character in given_string:
            given_string = given_string.replace(character, "")

    return given_string


json_for_classes = open("classes_parsed.json", "r")
json_for_classes = json.loads(json_for_classes.read())


def generate_program_array():
    for entry in json_for_classes:
        if entry['class'].get('subject') not in programs:
            programs.append(entry['class'].get('subject'))

    print(programs)


if __name__ == "__main__":
    generate_program_array()