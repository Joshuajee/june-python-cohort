from rembg import remove
from datetime import datetime

input_path = "online.png"

output_path =  f"img-{datetime.now()}.jpg"

input_file = open(input_path, "rb")
output_file = open(output_path, "wb")

bg_remove = remove(input_file.read())

output_file.write(bg_remove)

input_file.close()
output_file.close()

