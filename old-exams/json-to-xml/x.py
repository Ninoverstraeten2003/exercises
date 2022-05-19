import json
from pprint import pprint
import xml.etree.ElementTree  as ET
import re

with open('input.json', 'r') as f:
    content = json.load(f)
    
    def list_dict_to_xml(tag, list):
        elem = ET.Element(tag)
        for dict in list:
            # create an Element
            # class object

            child = ET.Element('student')
            child.set('id',dict['id'])
            sub_grades = ET.SubElement(child,'grades')
            for i in dict['grades']:
                sub = ET.SubElement(sub_grades,'grade')
                sub.text = str(i)
            elem.append(child)

        return elem

    # e stores the element instance
    with open('output.txt','w') as f:
        e =list_dict_to_xml('students', content)
        out = ET.tostring(e, encoding='utf8', method='xml').decode("utf-8").split('\n')[1]
        match = re.findall(r'<student id=\"\D\d*\">.*?</student>',out)
        f.write("<students>\n")
        for i in match:
            f.write(f'{i}\n')
        f.write("</students>")
       

 
  

