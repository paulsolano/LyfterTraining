student_information = {
    "name": "Harry",
    "lastname": "Potter",
    "age": 17
}

deleted_item = student_information.pop("lastname")
print(student_information)
print(f"El apellido eliminado es: {deleted_item}")