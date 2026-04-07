from PIL import Image

# ----------------------------
# FUNÇÃO — Upscale 2x
# (equivalente ao Step 4 completo)
# ----------------------------

def upscale_2x(img):

    width, height = img.size
    pixels = img.load()

    # Nova imagem (2x maior)
    new_width = width * 2
    new_height = height * 2

    new_img = Image.new(
        "RGB",
        (new_width, new_height),
        (0, 0, 0)
    )

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

    return new_img


# ----------------------------
# CONFIGURAÇÃO
# ----------------------------

input_path = "../input/input.png"
output_path = "../output/output_step5_iterative.png"

# Número de repetições
# 4 iterações = 16x escala final

iterations = 2

# Segurança contra explosão de memória

max_iterations = 2

if iterations > max_iterations:
    raise ValueError(
        "Número máximo de iterações excedido."
    )

# ----------------------------
# EXECUÇÃO ITERATIVA
# ----------------------------

img = Image.open(input_path).convert("RGB")

print("Imagem inicial:", img.size)

for i in range(iterations):

    print(
        "Iteração",
        i + 1,
        "- Tamanho atual:",
        img.size
    )

    img = upscale_2x(img)

    print(
        "Nova dimensão:",
        img.size
    )


# ----------------------------
# SALVAR RESULTADO FINAL
# ----------------------------

img.save(output_path)

print("Imagem final salva em:", output_path)