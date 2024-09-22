import base64

# Replace 'your_file.png' with the path of the file you want to convert
with open("C:/Users/saidh/flask_backendfile.jpeg", "rb") as file:
    encoded_string = base64.b64encode(file.read()).decode('utf-8')

# Print the Base64 string
print(encoded_string)
