def create_files_dict(file_1, file_2, file_3):
    
    files_list = [file_1, file_2, file_3]
    files_dict = {}
    
    for file in files_list:
        
        with open(file, encoding='utf-8') as file_in_the_process:
            strings_quantity = len(file_in_the_process.readlines())
        with open(file, encoding='utf-8') as file_in_the_process:
             content = file_in_the_process.read()
            
        files_dict[file] = [strings_quantity, content]
    
    return files_dict

print(create_files_dict('1.txt', '2.txt', '3.txt'))