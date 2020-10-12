from pathlib import Path
import os
import json


class Conf:
    def __init__(self, inputdata=None):
        self.filename = "conf.json"
        self.inputdata = inputdata

    def Check_file(self) -> bool:
        conffile = Path(os.path.join(os.getcwd(), self.filename))

        return conffile.is_file()

    def Get_config(self):
        try:
            with open(self.filename) as f:
                data = json.load(f)
            return data
        except:
            pass

    def Save_config(self) -> bool:
        result = False
        try:
            with open(self.filename, "w") as outfile:
                json.dump(self.inputdata, outfile)
            result = True
        except:
            pass

        return result

