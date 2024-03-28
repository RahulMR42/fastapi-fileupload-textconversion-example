import textract


class Files:
    def __init__(self):
        self.input_path = 'inputs'

    def convert_to_text(self, file_name):
        try:
            converted_text = textract.process(f"{self.input_path}/{file_name}")
            print(converted_text)
        except Exception as e:
            print(e)
