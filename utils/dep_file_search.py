def dep_search(file_to_check, files_inform, folder_inform,visited=None,tupled_dependencies=None):
    dependencies = set()
    if visited is None:
        visited = set()
    parent_folder = None
    if tupled_dependencies is None:
        tupled_dependencies = []
    visited.add(file_to_check)
    for folder in folder_inform:
        if folder['folder_files'] == file_to_check:
            parent_folder = folder['folder_name']#if there is any folder name there.
            break 

    for file_info in files_inform:
        if file_to_check in file_info['imp']:
            dependencies.add(file_info['file_name'])  # Direct dependency
    
    if parent_folder:
        for file_info in files_inform:
            if parent_folder in file_info['imp']:
                dependencies.add(file_info['file_name'])  

    for imp_file in list(dependencies):
        if imp_file not in visited:
            new_dependencies, new_tupled_dependencies = dep_search(imp_file, files_inform,folder_inform,visited, tupled_dependencies)
            dependencies.update(new_dependencies)#here we updating the dependencies only. 
    result = [(file_to_check, item) for item in dependencies]#creating a list of tuple
    tupled_dependencies.extend(result)
 
    
    return list(dependencies),tupled_dependencies