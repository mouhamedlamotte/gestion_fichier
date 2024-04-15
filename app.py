import os
from flask import Flask, render_template, request
from constant import FORMAT
from manage import Manage

mf = Manage()


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", formats=FORMAT)


@app.route("/file", methods=['POST'])
def file():
    try :
        file = request.files['file']
        type_file = mf.get_file_type(file.filename)
        if type_file is None:
            return render_template("not_supported.html", message =f"le type de fichier {file.filename} n'est pas supporte")
        type_format = type_file["format"]
        file.save(f"uploads/{type_format}/{file.filename}")
        size = request.content_length
        file_info = {
            "filename": file.filename,
            "size": size,
            "type": file.content_type,
            "image": type_file["image"]
        }
        
        other_extention = mf.get_other_format(type_format)
        
        
        rows = None
        columns = None
        data, keys = mf.get_rows_colums(type_format,f"uploads/{type_format}/{file.filename}")

        type_data = "dict" if isinstance(data, dict) else "list"
        json_download = mf.data_to_json(data, file.filename.split(".")[0])
        csv_download  = mf.data_to_csv(data, file.filename.split(".")[0])
        try :
            return render_template("file_info.html", file_info=file_info, other_extention=other_extention , columns=keys, rows=data, type_data= type_data, json_download=json_download, csv_download=csv_download)
        except Exception as e:
            return render_template("file_info.html", file_info=file_info, other_extention=other_extention)
            
    except Exception as e:
        print("error in file", e)
        return render_template("not_supported.html", message =f"une erreur est survenue {e}")


if __name__ == "__main__" :
    app.run(debug=True)
