def content_reader(file_path):
    try:
        with open(file_path, "r") as file:
            content_y = file.readlines()
            content_y = [line.strip() for line in content_y  if line.startswith(("import","package"))]
        return content_y
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

#sahjaskksjaks