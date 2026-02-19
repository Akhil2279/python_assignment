
import unittest
from unittest.mock import patch
from src.validating_email_adress_with_filter.util import filter_mail

class TestFilterMail(unittest.TestCase):

    @patch("builtins.input")
    def test_valid_emails(self, mock_input):

        mock_input.side_effect = [
            "4",
            "abc@gmail.com",
            "invalid-email",
            "user_123@yahoo.in",
            "wrong@com"
        ]

        result = filter_mail()
        self.assertEqual(result, ["abc@gmail.com", "user_123@yahoo.in"])

if __name__ == "__main__":
    unittest.main()


