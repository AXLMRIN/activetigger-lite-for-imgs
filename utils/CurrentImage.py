import pandas as pd 
from .function import get_available_images, get_labels

class CurrentImage:
    def __init__(self):
        self.available_images = get_available_images()
        self.max_value = len(self.available_images)
        
        self.available_labels = get_labels()

        self.df = pd.read_csv("./annotations.csv")

        # dynamic variables
        self.current_index = 0
        self.label = None
        self.image_name = None

        self.update()

    def update(self):
        self.image_name = self.available_images[self.current_index]
        index_current_path = self.df["id"] == self.image_name
        if index_current_path.sum() == 1:
            self.label = str(self.df.loc[index_current_path, "label"].item())
        elif index_current_path.sum() == 0:
            self.label = None
        else:
            self.label = "ERREUR, this image has multiple labels"
            print("Houston we've got a problem")
            print(self.df.loc[index_current_path, :])
    
    def set_available_images(self, available_images):
        self.available_images = available_images

    def next(self):
        self.current_index = (self.current_index + 1) % self.max_value
        self.update()

    def previous(self):
        self.current_index = (self.current_index - 1) % self.max_value
        self.update()

    def save_label(self, new_label):
        index_current_path = self.df["id"] == self.image_name
        if index_current_path.sum() == 1:
            self.df.loc[index_current_path, "label"] = new_label
            self.df.to_csv("./annotations.csv")
        elif index_current_path.sum() == 0:
            self.df.loc[len(self.df)] = {"id":self.image_name, "label":new_label}
        else:
            print("Houston we've got a problem")
            print(self.df.loc[index_current_path, :])
        self.df.to_csv("./annotations.csv", index = False)
        self.update()