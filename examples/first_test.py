import core.parser as parser
import core.display as display
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

response = parser.parse_json(response)
response = response[0]

display.print_json_as_list(response)