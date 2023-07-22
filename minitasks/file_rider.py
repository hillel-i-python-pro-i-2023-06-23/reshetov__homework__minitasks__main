def reader(filename: str) -> str:
    """
    :param: filename: name of your file
    :return: contents of your file
    """
    with open(filename) as file_object:
        text = file_object.read()
        print(text)
        return text
