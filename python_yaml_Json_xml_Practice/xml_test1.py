#import xml.etree.ElementTree as ET
import xmltodict 
from pprint import pprint

with open("xml_with_list2.xml") as data:
    read_xml=data.read()

my_dict = xmltodict.parse(read_xml)
#my_dict = xmltodict.parse("xml_with_list1.xml")

#pprint(my_dict)
#pprint(my_dict["champ_info"]["Address"]["Forest_Hill"])
pprint(my_dict["root"]["object"]["array"][0])
