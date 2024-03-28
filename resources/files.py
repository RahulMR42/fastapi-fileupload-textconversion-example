from resources.genai import Genai
import textract
import uuid
import os

class Files:
    def __init__(self, tmp_input_path, tmp_output_path, compartment_ocid):
        self.compartment_ocid = compartment_ocid
        self.input_path = tmp_input_path
        self.output_path = tmp_output_path
        Files.create_dir(self.input_path)
        Files.create_dir(self.output_path)

    @staticmethod
    def create_dir(path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)

        except Exception as e:
            print(e)

    def convert_to_text(self, file_name):
        try:
            converted_text = textract.process(f"{self.input_path}/{file_name}")
            file_id = str(uuid.uuid4().hex)
            with open(f"{self.output_path}/{file_id}.txt", 'wb+') as file:
                file.write(converted_text)

            genai_object = Genai(self.compartment_ocid)
            summary_text = genai_object.summerise_text(converted_text.decode('utf-8'))
            return file_id, summary_text
        except Exception as e:
            print(e)
