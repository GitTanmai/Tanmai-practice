import os
import re
from datetime import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
#        print(file)
#        print(re.search('\d{8}', file))
        fl = re.search('\d{8}', file)
        if fl is None:
            pass
        else:
            if fl.group() == datetime.today().date().strftime("%d%m%Y"):
                print(file)
