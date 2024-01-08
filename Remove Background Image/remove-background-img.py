from rembg import remove
from PIL import Image

input_path = 'rj_macready.jpeg'
output_path = 'rj_macready.png'

input = Image.open(input_path)
output = remove(input)

output.save(output_path)
