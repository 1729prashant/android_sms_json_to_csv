-----------------------
Background
-----------------------
This project provides a way to convert sms from json format to a readable csv format. This is specific to the json file created by Samsung's SmartSwitch app when backing up call logs and sms messages in Galaxy devices. This is not an exhaustive solution to retrieve all backup data from your Samsung/android device. This project has programs that work on clear text data only.


-----------------------
Files & Use Case
-----------------------

FILE                       DESCRIPTION
android_json_to_csv.py   - Python program that converts Samsung SmartSwitch exported json file SMS data to csv file. All information is retained. 
                           Ensure that the input file "sms_restore.json" is kept in the same directory as this script.
                           Creates an output file "sms_restore.csv" containing sms data in csv format, in the same directory. Two extra columns are added in the output file for the dates to be displayed in human readable format, as the default date format is unix epoch. Data is sorted in ascending order by date, i.e. latest message appears at the top of the file.
                           Python command to run file: "python3 android_json_to_csv.py"                       
sms_restore.json         - Sample input file provided. Note that the names of contacts are not directly available in these files, only phone numbers are captured.
sms_restore.csv          - csv format output file.
android_vcf_csv.py       - Python program that converts vcf file format data to csv format. Multiple phone numbers for the same contact are displayed on separate rows. 
                           Requires that the "Contacts.vcf" file is kept in the same directory as this python script.
                           Creates an output file "Contacts.csv" containing contact data in csv format, in the same directory.
                           This program exists solely to create phone numbers and names in csv formats which can aid in vlookups.
                           Python command to run file: "python3 android_vcf_csv.py"                       
Contacts.vcf             - Sample file with data of contacts in vcf format.
Contacts.csv             - csv format output file of name, phone number and email. 


-----------------------
Additional Information
-----------------------
Below is the folder structure of the backups exported by the Samsung SmartSwitch app. Note that majority of the data is encrypted in these files making it extremely hard to recover your own files without another Samsung device. Even if you export data without selecting the encryption,, most of the data is still encrypted. What we are interested in is the "sms_restore.json" file, see the below tree to find the folder in which you can find the same. This project does not cover decryption of the files or how to read the ".bk" file formats. I do not have information on how Samsung does the encryptions. The only alternative to read this file is to have another Samsung Galaxy device and import the backup.


SmartSwitchBackup
└── 2222222222222
    ├── APKDENYLIST
    │   └── APKDENYLIST.zip
    ├── APKFILE
    │   ├── AppList.bk
    │   ├── com.whatsapp.enc
    ├── CALLLOG
    │   ├── CALLLOG.zip
    │   ├── call_log.exml
    │   └── com.samsung.android.dialer.png_
    ├── CALLOGSETTING
    │   └── CALLOGSETTING.zip
    ├── CONTACT
    │   ├── CONTACT_JSON
    │   │   ├── youremail@address.com-com.google
    │   │   │   ├── youremail@address.com-com.google.json.enc
    │   │   │   ├── Google.icon
    │   │   │   ├── blob
    │   │   │   │   ├── 1596_15
    │   │   │   │   ├── 1654_15
    │   │   │   │   ├── 1667_15
    │   │   │   └── image
    │   │   │       ├── 11
    │   │   │       ├── 13
    │   │   │       ├── 6
    │   │   └── vnd.sec.contact.phone-vnd.sec.contact.phone
    │   │       ├── blob
    │   │       │   ├── 208_15
    │   │       │   ├── 222_15
    │   │       │   ├── 264_15
    │   │       ├── image
    │   │       │   ├── 1
    │   │       │   ├── 3
    │   │       │   └── 4
    │   │       └── vnd.sec.contact.phone-vnd.sec.contact.phone.json.enc
    │   ├── CONTACT_JSON.zip
    │   ├── Contact.bk
    │   └── com.samsung.android.app.contacts.png_
    ├── CONTACTSETTING
    │   └── CONTACTSETTING.zip
    ├── DIALERSETTING
    │   └── DIALERSETTING.zip
    ├── MESSAGE
    │   ├── MESSAGE_JSON.zip
    │   ├── Message.edb
    │   ├── PART_9999999999999_Office_Lens_20160101-224455
    │   ├── PART_9999999999999_20160101_224455
    │   ├── RCSMESSAGE
    │   │   └── RcsMessage.edb
    │   ├── com.samsung.android.messaging.png_
    │   ├── mms_restore.bk
    │   ├── mms_restore.json
    │   ├── sms_restore.bk
    │   └── sms_restore.json <-------------------------------- !! This is the file of interest !!
    ├── MESSAGESETTING
    │   └── MESSAGESETTING.zip
    ├── SHEALTH2
    │   ├── SHEALTH2.zip
    │   └── com.sec.android.app.shealth.png_
    ├── SMARTSWITCH_LOG
    │   ├── SmartSwitchLog_SM-N960F_2024-04-24_13_23_0.log
    │   └── SmartSwitchLog_SM-N960F_2024-04-24_13_23_0.zip
    ├── SmartSwitchBackup.bk
    ├── SmartSwitchBackupInf.bk
    └── SmartSwitchBackupInf.bk_backup