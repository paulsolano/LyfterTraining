from unittest.mock import patch, mock_open

def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()

class TestReadLines:
    def test_read_lines_returns_file_content(self):
        contenido_falso = "linea 1\nlinea 2\nlinea 3\n"
        with patch("builtins.open", mock_open(read_data=contenido_falso)):
            result = read_lines("cualquier_ruta.txt")
        assert result == ["linea 1\n", "linea 2\n", "linea 3\n"]

    def test_return_expected_lines_without_new_files(self):
        contenido_falso = "linea 1\nlinea 2\nlinea 3\n"
        with patch("builtins.open", mock_open(read_data=contenido_falso)):
            result = read_lines("cualquier_ruta.txt")
        assert result == ["linea 1\n", "linea 2\n", "linea 3\n"]

    def test_FileNotFoundError_is_raised_for_nonexistent_file(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            try:
                read_lines("archivo_inexistente.txt")
                assert False, "Se esperaba un FileNotFoundError, pero no ocurrió"
            except FileNotFoundError:
                pass