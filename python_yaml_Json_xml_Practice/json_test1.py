import json
from pprint import pprint

with open("int_Conf_DevBk.json") as my_json_file:

	#print(my_json_file)

	pprint(json.load(my_json_file)["interface"]["ipv4"]["address"][1])
	#pprint(json.load(my_json_file)["interface_details"][1])
	#my_file= my_json_file.read()
	#print(my_file)
	

	
	#file_contents = json.loads(my_file)
	#print(file_contents.keys())

	#for my_keys, my_values in file_contents.items():
	#	print(my_keys)
	#	print(my_values)
	