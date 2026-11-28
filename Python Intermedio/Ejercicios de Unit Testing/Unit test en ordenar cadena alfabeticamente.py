def order_string_alphabetically(s):
    return "-".join(sorted(s.split("-")))

def test_order_string_alphabetically():
    assert order_string_alphabetically("banana-apple-cherry") == "apple-banana-cherry"
    assert order_string_alphabetically("zebra-elephant-dog") == "dog-elephant-zebra"
    assert order_string_alphabetically("grape-orange-kiwi") == "grape-kiwi-orange"
    assert order_string_alphabetically("") == ""
    assert order_string_alphabetically("singleword") == "singleword"
    assert order_string_alphabetically("a-b-c-d-e") == "a-b-c-d-e"

def test_order_string_alphabetically_with_special_characters():
    assert order_string_alphabetically("banana-apple-cherry!") == "apple-banana-cherry!"
    assert order_string_alphabetically("zebra-elephant-dog@") == "dog@-elephant-zebra"
    assert order_string_alphabetically("grape-orange-kiwi#") == "grape-kiwi#-orange"
    assert order_string_alphabetically("!@#$%^&*()") == "!@#$%^&*()"
    assert order_string_alphabetically("a-b-c-d-e!") == "a-b-c-d-e!"

def test_order_string_alphabetically_with_numbers():
    assert order_string_alphabetically("banana-apple-123") == "123-apple-banana"
    assert order_string_alphabetically("zebra-elephant-456") == "456-elephant-zebra"
    assert order_string_alphabetically("grape-orange-789") == "789-grape-orange"

if __name__ == "__main__":
    print("Ejercicio 6 - Funciones")
    ordered_string = order_string_alphabetically(input("Escribe la cadena de texto: "))
    print("La cadena ordenada alfabéticamente es: ", ordered_string)
