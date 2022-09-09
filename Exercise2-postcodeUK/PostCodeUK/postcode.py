import os
import sys
import re
import json
import  gzip

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\" + "Database"
db_name = 'postcodes.gz'

class PostCode:

    def load_database(self):
        postcodes = []
        with gzip.open('{}\\{}'.format(BASE_DIR, db_name), 'rt') as infile:
            for key, val in json.load(infile).items():
                for v in val.split(","):
                    postcodes.append(key + v)
        return postcodes

    def validate_postcode_Regex(self, pc_formatted):

        pattern = re.compile('^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{3}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$')
        if pattern.match(pc_formatted):
            print('PostCode Validation Successful!')
            return True
        else:
            print('PostCode Validation Unsuccessful!')
            return False

    def validate_postcode(self, pc_formatted):
        pc_db = self.load_database()
        if pc_formatted in pc_db:
            print(pc_formatted + " is in the Database")
            return True
        else:
            print(pc_formatted + " is not in the Database")
            return False


if __name__ == '__main__':
    pcObj = PostCode()
    pcName = sys.argv[1]
    pcName = pcName.upper()
    if ' ' in pcName:
        pcName = pcName.replace(" ", "")
    pcObj.validate_postcode_Regex(pcName)
    pcObj.validate_postcode(pcName)






