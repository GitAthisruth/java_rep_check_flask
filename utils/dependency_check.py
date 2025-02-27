from utils.dep_file_search import dep_search
from utils.get_file_imports import get_imports
from utils.content_reader import content_reader
import json
import os


def dependency_check(folder_path,file_to_check):
    file_inform = []
    folder_inform = []
    all_files = []
    imp_list = []
    extensions = ('.java')

    if file_to_check.endswith(extensions):
        file_to_check = os.path.splitext(file_to_check)[0]#convert file without extension
            
   
    all_files.extend(os.path.splitext(os.path.basename(file))[0] for file in glob(os.path.join(folder_path, '**', f'*{".java"}'), recursive=True))
    for (dirpath,dirnames, filenames) in os.walk(folder_path):
        for file in filenames:
            if file.endswith(extensions):
                file_path = os.path.join(dirpath, file)
                file_contents = content_reader(file_path)
                if file_contents:
                    file_imports = get_imports(file_contents)
                    if "package" in file_imports[0]:
                        package_name = file_imports[0].replace("package ", "").replace(";", "").strip()
                        folder_inform.append({"folder_name":package_name,"folder_files":file.split(".")[0]})
                    else:    
                        file_inform.append({"file_name":file.split(".")[0],"imp":file_imports})
    result = dep_search(file_to_check,file_inform,folder_inform)
    imp_list = result[0]
    imp_list_json = json.dumps({"file": file_to_check, "dependencies": imp_list}, indent=4)
    with open(f"{file_to_check}_dependencies.json", "w") as outfile:
        outfile.write(imp_list_json)
    with open(f'{file_to_check}_txt_file_info.txt', 'w') as file:
        file.write(imp_list_json)
        
    
    return imp_list_json




