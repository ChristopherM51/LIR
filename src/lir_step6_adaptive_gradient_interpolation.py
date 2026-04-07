# LIR Step 6
# Adaptive gradient interpolation using full-pixel RGB averaging.
# Gradient dominance applied to averaged RGB values.

from PIL import Image

# ============================
# CONFIGURAÇÃO EXPERIMENTAL
# ============================

THRESHOLD = 150

WEIGHT_HIGH = 0.9
WEIGHT_LOW = 0.1
WEIGHT_NORMAL = 0.5

# ============================
# FUNÇÕES
# ============================

def adaptive_channel(v1, v3):

    diff = v3 - v1

    if diff > THRESHOLD:

        return int(
            v1 * WEIGHT_LOW +
            v3 * WEIGHT_HIGH
        )

    elif diff < -THRESHOLD:

        return int(
            v1 * WEIGHT_HIGH +
            v3 * WEIGHT_LOW
        )

    else:

        return int(
            v1 * WEIGHT_NORMAL +
            v3 * WEIGHT_NORMAL
        )


def adaptive_pixel(p1, p3):

    r = adaptive_channel(p1[0], p3[0])
    g = adaptive_channel(p1[1], p3[1])
    b = adaptive_channel(p1[2], p3[2])

    return (r, g, b)

# ============================
# CAMINHOS
# ============================

input_path = "../input/input.png"
output_path = "../output/output_adaptive.png"

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

        new_pixels[x, y] = adaptive_pixel(
            left,
            right
        )

# ----------------------------
# PASSO 3 — Vertical
# ----------------------------

for y in range(1, new_height - 1, 2):
    for x in range(0, new_width):

        top = new_pixels[x, y - 1]
        bottom = new_pixels[x, y + 1]

        new_pixels[x, y] = adaptive_pixel(
            top,
            bottom
        )

print("Preenchimento adaptativo completo.")

# Salvar
new_img.save(output_path)

print("Imagem salva em:", output_path)