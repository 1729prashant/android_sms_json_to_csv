import unittest
from datetime import datetime
import json
import os
import csv

# Import functions to test
from android_json_to_csv import load_json, get_headers, convert_unix_to_human, write_json_to_csv

class TestSMSJsonToCSV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary JSON file for testing
        cls.test_json_file = os.getcwd() + "/" + 'test_sms.json'
        cls.test_json_data = [
            {"date": 1617846000000, "date_sent": 1617846010000, "sender": "Alice", "message": "Hello"},
            {"date": 1617846020000, "date_sent": 1617846030000, "sender": "Bob", "message": "Hi"}
        ]
        with open(cls.test_json_file, 'w') as f:
            json.dump(cls.test_json_data, f)

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary JSON file after testing
        os.remove(cls.test_json_file)

    def test_load_json(self):
        # Test loading JSON file
        loaded_data = load_json(self.test_json_file)
        self.assertEqual(loaded_data, self.test_json_data)

        # Test for empty file
        with open(os.getcwd() + "/" + 'empty_file.json', 'w') as f:
            f.write('')
        loaded_empty_data = load_json(os.getcwd() + "/" + 'empty_file.json')
        self.assertIsNone(loaded_empty_data)

        # Test for non-existent file
        non_existent_file = os.getcwd() + "/" + 'non_existent_file.json'
        self.assertIsNone(load_json(non_existent_file))

    def test_get_headers(self):
        # Test getting headers from JSON data
        headers = get_headers(self.test_json_data)
        expected_headers = ['date', 'date_sent', 'message', 'sender']
        self.assertEqual(headers, expected_headers)

        # Test for empty JSON data
        empty_data = []
        self.assertEqual(get_headers(empty_data), [])

        # Test for JSON data with different headers
        json_data_diff_headers = [
            {"date": 1617846000000, "sender": "Alice", "message": "Hello"},
            {"date_sent": 1617846020000, "sender": "Bob", "message": "Hi"}
        ]
        expected_headers_diff = ['date', 'date_sent', 'message', 'sender']
        self.assertEqual(get_headers(json_data_diff_headers), expected_headers_diff)

    def test_convert_unix_to_human(self):
        # Test converting Unix timestamp to human-readable format
        timestamp = 1617846000000  # 2021-04-07 12:00:00 UTC
        converted_date = convert_unix_to_human(timestamp, 1)
        expected_date = datetime.utcfromtimestamp(timestamp / 1000).strftime('%d/%m/%Y %H:%M:%S')
        self.assertEqual(converted_date, expected_date)

        # Test for empty timestamp
        self.assertEqual(convert_unix_to_human('', 1), '')

        # Test for invalid timestamp
        self.assertIsNone(convert_unix_to_human('invalid_timestamp', 1))

    def test_write_json_to_csv(self):
        # Test writing JSON data to CSV
        test_csv_file = os.getcwd() + "/" + 'test_sms.csv'
        headers = ['date', 'date_sent', 'message', 'sender']
        write_json_to_csv(self.test_json_data, headers, test_csv_file)
        # Check if CSV file exists
        self.assertTrue(os.path.exists(test_csv_file))
        # Check if CSV file has correct data
        with open(test_csv_file, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), len(self.test_json_data))
            for i, row in enumerate(rows):
                for key, value in row.items():
                    self.assertEqual(value, str(self.test_json_data[i][key]))

        # Remove the temporary CSV file after testing
        os.remove(test_csv_file)

        # Test for empty JSON data
        empty_data = []
        empty_csv_file = os.getcwd() + "/" + 'empty_test.csv'
        write_json_to_csv(empty_data, [], empty_csv_file)
        self.assertTrue(os.path.exists(empty_csv_file))
        with open(empty_csv_file, 'r') as f:
            reader = csv.DictReader(f)
            self.assertEqual(len(list(reader)), 0)
        os.remove(empty_csv_file)

if __name__ == '__main__':
    unittest.main()

