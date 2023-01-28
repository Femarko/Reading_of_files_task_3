class FilesProcessor:
    def __init__(self, files_names_list):
        self.files_names_list = files_names_list

    def create_files_dict(self):
        
        files_dict = {}
        
        for file in self.files_names_list:
            
            with open(file, encoding='utf-8') as file_in_the_process:
                strings_quantity = len(file_in_the_process.readlines())
            with open(file, encoding='utf-8') as file_in_the_process:
                content = file_in_the_process.read()
                
            files_dict[file] = [strings_quantity, content]
        
        return files_dict

processor = FilesProcessor(['1.txt', '2.txt', '3.txt'])
print(processor.create_files_dict())