# ==========================================================
# LIR Step 1 — Pixel Extraction
#
# Reads the source image and converts it to RGB format.
# Loads pixel data into memory for direct access.
#
# Purpose:
# Establish low-level access to pixel values,
# enabling manual reconstruction logic.
#
# Key concept introduced:
# Direct pixel reading and manipulation.
# ==========================================================

from PIL import Image

# Caminho da imagem
image_path = "../input/input.png"

# Abrir imagem
img = Image.open(image_path).convert("RGB")

# Obter dimensões
width, height = img.size

# Acessar pixels
pixels = img.load()

print("Dimensões da imagem:")
print(width, "x", height)

print("\nPrimeiros pixels:")

# Ler alguns pixels
for y in range(3):
    for x in range(3):

        r, g, b = pixels[x, y]

        print(
            f"Pixel ({x},{y}) -> "
            f"R:{r} G:{g} B:{b}"
        )