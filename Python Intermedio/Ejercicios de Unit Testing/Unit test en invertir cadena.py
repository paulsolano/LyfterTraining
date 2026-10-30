def reverse_string(s):
    return s[::-1]

def test_reverse_string():
    assert reverse_string("Hola Mundo") == "odnuM aloH"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"

def test_reverse_string_with_special_characters():
    assert reverse_string("Hola, Mundo!") == "!odnuM ,aloH"
    assert reverse_string("¡Hola! ¿Cómo estás?") == "?sátse omóC¿ !aloH¡"
    assert reverse_string("1234!@#$") == "$#@!4321"
    assert reverse_string("H1o2l3a!") == "!a3l2o1H"

def test_reverse_string_with_spaces():
    assert reverse_string("Hola Mundo") == "odnuM aloH"
    assert reverse_string("Python es un lenguaje de programación") == "nóicamargorp ed ejaugnel nu se nohtyP"
    assert reverse_string("   ") == "   "


if __name__ == "__main__":
    print("Ejercicio 4 - Funciones")
    input_string = input("Ingresa una cadena de texto: ")
    reversed_string = reverse_string(input_string)
    print(f"La cadena invertida es: {reversed_string}")
