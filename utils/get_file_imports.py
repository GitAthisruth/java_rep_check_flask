# all_file_path = [{'file_name': 'setup.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\setup.py'}, {'file_name': 'environment.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\importlab\\environment.py'}, {'file_name': 'fs.py', 'file_path': 'C:\\Users\\LENOVO\\Desktop\\flask_app_for_dep\\flask_app_for_dep_checker\\test\\importlab\\importlab\\fs.py'}]
import re

def get_imports(content):
    try:
        imports = []
        for val in content:
            regex = r"(?:import\s+([\w]+(?:\.[\w]+)*)(?:\.\*|;)?)|((package)\s+([\w]+(?:\.[\w]+)?)\s*;)"
            matches = re.findall(regex,val)
            for match in matches:
                module_name = match[0] or match[1]
                if "." in module_name:
                    module_name_ = module_name.split(".")[-1]
                    imports.append(module_name_)
                else:
                    imports.append(module_name)
        return list(set(imports))    
    except Exception as e:
        print(f"An error occured while extracting imports: {e}")
        return []

# print(get_imports(all_file_path))