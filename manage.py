import datetime
import json
import yaml
import csv
from constant import FORMAT, EXTENSION


class Manage():
    def __init__(self):
        ...
        
    
    def get_file_type(self, filename : str):
        file_info = filename.split(".")
        ext = file_info[-1]
        if ext in EXTENSION.keys():
            return EXTENSION[ext]
        else :
            return None
        
        
    def get_other_format(self, current_format : str):
        new_ex = []
        for format in EXTENSION:
            if format.lower() != current_format.lower():
                new_ex.append(EXTENSION[format])
        return new_ex
    
    
    def read_json_file(self, file_path):
        data = []
        keys = []
        
        with open(file_path, 'r') as f:
            data = json.load(f)
        try :
            if isinstance(data, list):
                for k in data[0].keys():
                    keys.append(k)
            else :
                for k in data.keys():
                    keys.append(k)
        except Exception as e:
            print(e)
                
        return data, keys
    
    def read_csv_file(self, file_path):
        data = []
        keys = []
        try :
            with open(file_path, 'r') as f:
                d = csv.reader(f, delimiter=",")
                for l in d :
                    # print(l)
                    if len(keys) == 0:
                        keys = l
                    new_data = {
                        keys[j] : l[j] for j in range(len(l))
                    }
                    data.append(new_data)
                del data[0]
        except  Exception as e:
            print(e)
        # print(data)
        # print(keys)
        return data, keys
    
    def read_yaml_file(self, file_path):
        data = keys = []
        try :
            with open(file_path, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                # print("data is", data)
                # print("len keys", len(keys))
                
                if isinstance(data, list) :
                    keys = list(data[0].keys())
                else :
                    keys = list(data.keys())
        except Exception as e:
            print("erreur read yaml", e)
        return data, keys
        
    
    
    def get_rows_colums(self, file_format : str, file_path: str):
        data = keys = []
        print(file_format)
        if file_format.upper() == "JSON":
            data, keys = self.read_json_file(file_path)
        elif file_format.upper() == "CSV" :
            data, keys = self.read_csv_file(file_path)
        elif file_format.upper() == "YAML" :
            data, keys = self.read_yaml_file(file_path)
        return data, keys
    
    
    def data_to_json(self, data, filename):
        datetim = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        d_url = f"static/downloads/{filename}-{datetim}.json"
        with open(d_url, 'w') as f:
            json.dump(data, f, indent=4)
        return d_url
        
    def data_to_csv(self, data, filename):
        datetim = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        d_url = f"static/downloads/{filename}-{datetim}.csv"
        with open(d_url, 'w') as f:
            # print("here")
            keys = data[0].keys() if isinstance(data, list) else data.keys()
            # print(keys)
            writer = csv.DictWriter(f, keys)
            # print("writing done")
            writer.writeheader()
            for line in data:
                try :
                    writer.writerow(line)
                except Exception as e:
                    print(e)
                # f.write(','.join(line) + "\n")
            # print("done")
        return d_url
        
            
        