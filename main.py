import json

#Saving dictionary in a JSON file
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
 
with open("company1.json", "w") as file:
    json.dump(d, file, indent=4)
print("Dict >> JSON Completed")

#Add/Update JSON File
with open("company1.json", "r+") as file:
  d = json.loads(file.read())
  d["employees"].append(dict(firstName = "Albert", lastName = "Toto"))
  file.seek(0)
  json.dump(d, file, indent=4, sort_keys=True)
  file.truncate()
print("JSON updated")