# ==========================================================
# LIR Step 4 — Vertical Interpolation
#
# Reconstructs missing pixels between known
# vertical neighbors.
#
# New pixels are placed between:
# top → bottom
#
# Purpose:
# Restore vertical continuity.
#
# Key concept introduced:
# Linear interpolation along Y axis.
# ==========================================================

from PIL import Image
import time

# ============================
# INÍCIO DO CRONÔMETRO
# ============================

start_time = time.perf_counter()

# Caminhos
input_path = "../input/input.png"
output_path = "../output/output_step4_full.png"

# Abrir imagem
img = Image.open(input_path).convert("RGB")

width, height = img.size
pixels = img.load()

# Nova imagem
new_width = width * 2
new_height = height * 2

new_img = Image.new("RGB", (new_width, new_height), (0, 0, 0))
new_pixels = new_img.load()

# ----------------------------
# PASSO 1 — Pixels originais
# ----------------------------
for y in range(height):
    for x in range(width):

        new_pixels[x*2, y*2] = pixels[x, y]

# ----------------------------
# PASSO 2 — Horizontal
# ----------------------------
for y in range(0, new_height, 2):
    for x in range(1, new_width - 1, 2):

        left = new_pixels[x - 1, y]
        right = new_pixels[x + 1, y]

        r = (left[0] + right[0]) // 2
        g = (left[1] + right[1]) // 2
        b = (left[2] + right[2]) // 2

        new_pixels[x, y] = (r, g, b)

# ----------------------------
# PASSO 3 — Vertical
# ----------------------------
for y in range(1, new_height - 1, 2):
    for x in range(0, new_width):

        top = new_pixels[x, y - 1]
        bottom = new_pixels[x, y + 1]

        r = (top[0] + bottom[0]) // 2
        g = (top[1] + bottom[1]) // 2
        b = (top[2] + bottom[2]) // 2

        new_pixels[x, y] = (r, g, b)

print("Preenchimento completo.")

# Salvar
new_img.save(output_path)

# ============================
# FIM DO CRONÔMETRO
# ============================

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Imagem salva em:", output_path)
print(f"Tempo de execução: {elapsed_time:.6f} segundos")