import csv
import os
from actions import general_info
def export(filename="data.csv"):
    if not general_info:
        print("There are not registered students")
        return
    head=["name","section","spanish","english","social","science","average"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer= csv.DictWriter(file,head)
            writer.writeheader()
            writer.writerows(general_info)
        print(f"File successfully export to {filename}")
    except Exception as information:
        print(f"The error {information}")


def import_CSV(filename="data.csv"):
    if not os.path.exists(filename):
        print(f"Theres no files {filename}")
        return
    
    try:
        with open(filename, mode="r",newline="",encoding="utf-8") as f:
            reader=csv.DictReader(f)
            need={"name","section","spanish","english","social","science"}
            missed= need-set(reader.fieldnames or [])
            if missed:
                print(f"The file does not have the necessary columns")
            return

        count_before= len(general_info)
        for lines in reader:
            try:
                spanish = float(lines["spanish"])
                english = float(lines["english"])
                social  = float(lines["social"])
                science = float(lines["science"])
                trainers = {
                        "name": lines["name"].strip(),
                        "section": lines["section"].strip(),
                        "spanish": spanish,
                        "english": english,
                        "social": social,
                        "science": science,
                        "average": (spanish + english + social + science) / 4
                    }
                general_info.append(trainers)
            except(KeyError, ValueError) as mistake:
                print(f"the line is invalid, left out detail {mistake}")

            added = len(general_info) - count_before
            if added==0:
                print("there were not any files imported")
            else: 
                print(f"The importation was succeed: {added} added students")
    except Exception as no_imported:
        print(f"There was an error with the importation{no_imported}")

            