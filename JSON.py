import json

# json.loads(): used to convert JSON string to Python object
# json.dumps(): used to convert Python object to JSON string

json_str='{"name":"adarsh","isdeveloper":true}'
py_object=json.loads(json_str)
print(f"type of py_object after loads:{type(py_object)} and value:{py_object}")
# print(py_object)
# print(type(py_object))

json_obj=json.dumps(py_object)
print(f"type of json_obj after dumps:{type(json_obj)} and value:{json_obj}")


#when we  want to deal with files we use json.load() and json.dump()  
# json.load(): used to read JSON data from a file and convert it to a Python object
# json.dump(): used to write a Python object as JSON data to a file

with open("data.json","r") as f:
    py_file=json.load(f)
    print(f"type of py_file after load:{type(py_file)} and value:{py_file}")


d={"name":"adarsh","isdeveloper":True,"age":24}
with open("data.json","w") as f:
    json.dump(d,f,indent=4,sort_keys=True)
    print("data written to file successfully.")

with open("data.json","r") as f:
    py_file=json.load(f)
    print(f"type of py_file after load:{type(py_file)} and value:{py_file}")
