from unittest import TestCase

from src.libs.security.utils import file_to_base64


class TestFileBase64(TestCase):
    def test_file_to_base64(self):
        expected = (
            ""
        )
        file_name = "src/static/deeployr-logo-light.svg"
        result = file_to_base64(file_name)
        self.assertIn(expected, result)
        self.assertTrue(result.startswith(expected))
