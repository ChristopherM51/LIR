# ==========================================================
# LIR Step 3 — Horizontal Interpolation
#
# Reconstructs missing pixels between known
# horizontal neighbors.
#
# New pixels are placed between:
# left → right
#
# Purpose:
# Restore horizontal continuity.
#
# Key concept introduced:
# Linear interpolation along X axis.
# ==========================================================

from PIL import Image

# Caminhos
input_path = "../input/input.png"
output_path = "../output/output_step3_horizontal.png"

# Abrir imagem original
img = Image.open(input_path).convert("RGB")

width, height = img.size
pixels = img.load()

# Criar nova imagem (2x maior)
new_width = width * 2
new_height = height * 2

new_img = Image.new("RGB", (new_width, new_height), (0, 0, 0))
new_pixels = new_img.load()

# ----------------------------
# PASSO 1 — Colocar pixels originais
# ----------------------------

for y in range(height):
    for x in range(width):

        r, g, b = pixels[x, y]

        new_x = x * 2
        new_y = y * 2

        new_pixels[new_x, new_y] = (r, g, b)

# ----------------------------
# PASSO 2 — Preencher horizontalmente
# ----------------------------

for y in range(0, new_height, 2):

    for x in range(1, new_width - 1, 2):

        left_pixel = new_pixels[x - 1, y]
        right_pixel = new_pixels[x + 1, y]

        r = (left_pixel[0] + right_pixel[0]) // 2
        g = (left_pixel[1] + right_pixel[1]) // 2
        b = (left_pixel[2] + right_pixel[2]) // 2

        new_pixels[x, y] = (r, g, b)

print("Preenchimento horizontal concluído.")

# Salvar imagem
new_img.save(output_path)

print("Imagem salva em:", output_path)