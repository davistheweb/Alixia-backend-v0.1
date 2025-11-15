def getResponsibilities():
    try:
        with open("../responsibilities.txt", "r") as file:
            instruction = file.read()
            file.close()
            return instruction
    except Exception as e:
        return (f"Error loading responsibilities")