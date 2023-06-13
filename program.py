import sys
import json
import yaml
import xml.etree.ElementTree as ET

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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Sposób użycia: program.py pathFile1.x pathFile2.y")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input_extension = input_file.split(".")[-1].lower()
    output_extension = output_file.split(".")[-1].lower()

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
        print("Nieobsługiwane rozszerzenia plików.")
        sys.exit(1)

    with open(output_file, "w") as output:
        output.write(result)

    print(f"Konwersja z {input_extension} do {output_extension} zakończona pomyślnie.")
