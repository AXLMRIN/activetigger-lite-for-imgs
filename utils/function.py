import os 
import pandas as pd 

def get_available_images():
    return sorted(
        [
            filename
            for filename in os.listdir("./img")
            if filename.endswith((".png", ".jpg", ".jpeg"))
        ],
        key = None # Modify the key to change the order in which pictures must appear
    )

def remove_start_and_end_blank_spaces(label: str):
        while label.startswith(" "):
            label = label[1:]
        while label.endswith(" "):
            label = label[:-1]
        return label
    

def get_labels():
    with open("./labels.txt", "r") as file:
        labels = file.readlines()
    labels = [label.replace("\n", "") for label in labels]
    labels = [remove_start_and_end_blank_spaces(label) for label in labels]
    return ["NO LABEL"] + [label for label in labels if len(label)>0]

