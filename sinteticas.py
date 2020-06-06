from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

#retorna o endereço relativo dentro da pasta input
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.new("RGB", (700,700))

image.show()