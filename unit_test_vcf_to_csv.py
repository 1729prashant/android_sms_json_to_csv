import unittest
import os
from io import StringIO
from android_vcf_csv import vcf_to_csv

class TestVCFtoCSVConverter(unittest.TestCase):

    def setUp(self):
        # Create a sample VCF file for testing
        self.vcf_content = (
            "BEGIN:VCARD\n"
            "FN:John Doe\n"
            "TEL:123456789\n"
            "EMAIL:john@example.com\n"
            "END:VCARD\n"
            "BEGIN:VCARD\n"
            "FN:Jane Smith\n"
            "TEL:987654321\n"
            "EMAIL:jane@example.com\n"
            "END:VCARD\n"
        )
        self.test_vcf_file = 'test_contacts.vcf'
        with open(self.test_vcf_file, 'w') as f:
            f.write(self.vcf_content)

    def tearDown(self):
        # Remove the temporary VCF file after testing
        os.remove(self.test_vcf_file)

    def test_vcf_to_csv_conversion(self):
        # Test VCF to CSV conversion
        expected_csv_content = (
            "Name,Phone,Email\n"
            "John Doe,123456789,john@example.com\n"
            "Jane Smith,987654321,jane@example.com\n"
        )
        csv_output = StringIO()
        vcf_to_csv(self.test_vcf_file, csv_output)
        csv_output.seek(0)
        self.assertEqual(csv_output.getvalue(), expected_csv_content)

    def test_empty_vcf_file(self):
        # Test conversion with an empty VCF file
        empty_vcf_file = 'empty.vcf'
        with open(empty_vcf_file, 'w') as f:
            pass
        csv_output = StringIO()
        vcf_to_csv(empty_vcf_file, csv_output)
        csv_output.seek(0)
        self.assertEqual(csv_output.getvalue(), "Name,Phone,Email\n")

    def test_missing_vcf_file(self):
        # Test conversion with a missing VCF file
        missing_vcf_file = 'non_existent.vcf'
        csv_output = StringIO()
        vcf_to_csv(missing_vcf_file, csv_output)
        csv_output.seek(0)
        self.assertEqual(csv_output.getvalue(), "Name,Phone,Email\n")

if __name__ == '__main__':
    unittest.main()

