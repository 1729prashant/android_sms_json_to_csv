"""
vcf_to_csv_converter.py

This script converts vCard (VCF) files to CSV format. It extracts contact information such as name, phone number(s), and email address(es) from the VCF file and writes them into a CSV file.

Note: Customize the 'fieldnames' list in the vcf_to_csv function based on your specific requirements.

Author: Prashant V. Gaikar (@1729prashant)
Date: 24-APR-2024

Usage:
1. Place the VCF file named 'Contacts.vcf' in the same directory as this script.
2. Run the script. It will generate a CSV file named 'Contacts.csv' with the converted data.
"""

import csv
import os

def vcf_to_csv(vcf_file, csv_file):
    """
    Convert VCF (vCard) file to CSV format.

    Args:
        vcf_file (str): Path to the input VCF file.
        csv_file (str): Path to the output CSV file.

    Note:
        Customize the 'fieldnames' list based on your specific requirements.

    """
    with open(vcf_file, 'r', encoding='utf-8') as vcf:
        fieldnames = ['Name', 'Phone', 'Email']  # Customize based on your needs
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        name = ''
        phones = []
        email = ''
        for line in vcf:
            if line.startswith('FN'):
                name = line.strip().split(':', 1)[1]
            elif line.startswith('TEL'):
                phones.append(line.strip().split(':', 1)[1])
            elif line.startswith('EMAIL'):
                email = line.strip().split(':', 1)[1]
            elif line.strip() == 'END:VCARD':
                # Write a separate row for each phone number
                for phone in phones:
                    writer.writerow({'Name': name, 'Phone': phone, 'Email': email})
                # Reset variables for next contact
                name = ''
                phones = []
                email = ''



if __name__ == "__main__":
    current_directory = os.getcwd() + "/"
    print("Program running in: ", current_directory)
    vcf_path = current_directory

    vcf_file_path = vcf_path + "Contacts.vcf"
    csv_file_path = vcf_path + "Contacts.csv"

    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        vcf_to_csv(vcf_file_path, csv_file)
