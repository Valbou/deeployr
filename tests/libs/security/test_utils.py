from unittest import TestCase

from src.libs.security.utils import file_to_base64


class TestFileBase64(TestCase):
    def test_file_to_base64(self):
        expected = (
            "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iNDU1LjUybW0iIGhl"
        )
        file_name = "src/static/deeployr-light.svg"
        result = file_to_base64(file_name)
        self.assertIn(expected, result)
        self.assertTrue(result.startswith(expected))
