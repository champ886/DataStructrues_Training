from pprint import pprint
import yaml


with open("yaml_test1.yaml") as my_yaml_file:

	#print(my_yaml_file.yaml())["champ"]

	#my_file= my_yaml_file.read()
	#print(my_file)
	

	
	file_contents = yaml.load(my_yaml_file, Loader=yaml.FullLoader)
	
	
	# Just prints file contents as dictionaries
	#pprint(file_contents)
	#pprint(file_contents["champ_house"]["Array_1"])
	pprint(file_contents["object"]["array"][4])
	pprint(file_contents["paragraph"])

	#prints using "dict_keys" module
	#print(file_contents.keys())

	#for my_keys, my_values in file_contents.items():
		#print(my_keys)
		#print(my_values)
	