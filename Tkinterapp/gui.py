import customtkinter as ctk
import csv
from table import CTkTable

root = ctk.CTk()
root.title("Gestionaire de fichier ")
root.resizable(False, False)

main = ctk.CTkFrame(master=root)
main.grid(row=0, column=0)
main.update_idletasks()
width = main.winfo_width()
height = main.winfo_height()
root.geometry(f"{width}x{height}")



head = ctk.CTkFrame(master=main, fg_color="blue" ,height=60, width=1900 , corner_radius=0)
head.pack()

bloc_title = ctk.CTkFrame(master=main, fg_color="transparent", width=593, height=112)
bloc_title.pack(pady=10)

heading_1 = ctk.CTkLabel(master=bloc_title, text="Convertisseur de Fichier",justify="center", font=("inter", 46))
heading_1.pack(pady=5)

subhead = ctk.CTkLabel(master=bloc_title, text="Convertissez dans un autre format vos fichiers, en ligne, et gratuitement.", justify="center", font=("inter", 20))
subhead.pack(pady=20)

upload_box = ctk.CTkFrame(master=main, width=620, height=189, fg_color="#C7CECF", corner_radius=5)
upload_box.pack(pady=50) 
upload_box.pack_propagate(False)

table_container = ctk.CTkScrollableFrame(master=main, width=1100)


def create_table(values):
    rows = len(values)
    columns = len(values[0])
    
    table_container.pack()

    try :
        table = CTkTable(master=table_container, row=rows, column=columns, values=values)
        table.pack(expand=True, fill="both", padx=20, pady=20)
    except Exception as e:
        print(f"une erreurs s'est produite {e}")


def get_file():
    print("button pressed")
    file = ctk.filedialog.askopenfiles()
    file = file[0]
    val = []
    read = csv.reader(file)
    for l in read :
        val.append(l)
    if file :
        create_table(val)
        main.update_idletasks()
        width = main.winfo_width()
        height = main.winfo_height()
        root.geometry(f"{width}x{height}")
    

upload_button_box = ctk.CTkButton(master=upload_box, text="Upload file", width=271, height=65, fg_color="#147CF8", corner_radius=0, command=get_file)
upload_button_box.pack(anchor=ctk.CENTER, pady=20)
upload_box_subtext = ctk.CTkLabel(master=upload_box, text="Veillez choisir votre fichier à convertir (csv, json, xml, xsl, yaml)",  justify="center", font=("inter", 16), text_color="black")
upload_box_subtext.pack()


main.update_idletasks()
width = main.winfo_width()
height = main.winfo_height()
root.geometry(f"{width}x{height}")
root.mainloop()