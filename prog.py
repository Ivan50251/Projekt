import sys
import json
import yaml
import xml.etree.ElementTree as ET
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog

def convert_xml_to_json(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return json.dumps(data, indent=4)

def convert_json_to_xml(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        root = ET.Element("root")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        return ET.tostring(root, encoding="unicode")

def convert_json_to_yaml(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return yaml.dump(data)

def convert_yaml_to_json(yaml_path):
    with open(yaml_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
        return json.dumps(data, indent=4)

def convert_xml_to_yaml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return yaml.dump(data)

def convert_yaml_to_xml(yaml_path):
    with open(yaml_path) as yaml_file:
        data = yaml.safe_load(yaml_file)
        root = ET.Element("root")
        for key, value in data.items():
            element = ET.SubElement(root, key)
            element.text = str(value)
        return ET.tostring(root, encoding="unicode")

def browse_file(entry):
    file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml"), ("JSON Files", "*.json"), ("YAML Files", "*.yml")])
    if file_path:
        entry.delete(0, "end")
        entry.insert(0, file_path)

def convert_files():
    input_file = entry_input.get()
    output_file = entry_output.get()

    input_extension = input_file.split(".")[-1].lower()
    output_extension = output_file.split(".")[-1].lower()

    try:
        if input_extension == "xml" and output_extension == "json":
            result = convert_xml_to_json(input_file)
        elif input_extension == "json" and output_extension == "xml":
            result = convert_json_to_xml(input_file)
        elif input_extension == "json" and output_extension == "yml":
            result = convert_json_to_yaml(input_file)
        elif input_extension == "yml" and output_extension == "json":
            result = convert_yaml_to_json(input_file)
        elif input_extension == "xml" and output_extension == "yml":
            result = convert_xml_to_yaml(input_file)
        elif input_extension == "yml" and output_extension == "xml":
            result = convert_yaml_to_xml(input_file)
        else:
            messagebox.showerror("Błąd", "Nieobsługiwane rozszerzenia plików.")
            return

        with open(output_file, "w") as output:
            output.write(result)

        messagebox.showinfo("Sukces", f"Konwersja z {input_extension} do {output_extension} zakończona pomyślnie.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd podczas konwersji:\n{str(e)}")

if __name__ == "__main__":
    window = Tk()
    window.title("Konwerter danych")
    window.geometry("400x200")

    label_input = Label(window, text="Plik wejściowy:")
    label_input.pack()
    entry_input = Entry(window)
    entry_input.pack()
    button_browse_input = Button(window, text="Przeglądaj", command=lambda: browse_file(entry_input))
    button_browse_input.pack()

    label_output = Label(window, text="Plik wyjściowy:")
    label_output.pack()
    entry_output = Entry(window)
    entry_output.pack()
    button_browse_output = Button(window, text="Przeglądaj", command=lambda: browse_file(entry_output))
    button_browse_output.pack()

    button_convert = Button(window, text="Konwertuj", command=convert_files)
    button_convert.pack()

    window.mainloop()
