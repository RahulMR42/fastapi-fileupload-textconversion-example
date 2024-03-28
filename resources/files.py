import textract
import os


class Files:
    def __init__(self,tmp_input_path):
        self.input_path = tmp_input_path
        if not os.path.exists(self.input_path):
            os.makedirs(self.input_path)

    def convert_to_text(self, file_name):
        try:
            converted_text = textract.process(f"{self.input_path}/{file_name}")
            print(converted_text)
        except Exception as e:
            print(e)
