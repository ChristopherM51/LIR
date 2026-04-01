from PIL import Image

# Caminhos
input_path = "../input/input.png"
output_path = "../output/output_step2.png"

# Abrir imagem original
img = Image.open(input_path).convert("RGB")

width, height = img.size
pixels = img.load()

# Nova imagem com o dobro do tamanho
new_width = width * 2
new_height = height * 2

new_img = Image.new("RGB", (new_width, new_height), (0, 0, 0))

new_pixels = new_img.load()

print("Imagem original:", width, "x", height)
print("Nova imagem:", new_width, "x", new_height)

# Posicionar pixels originais
for y in range(height):
    for x in range(width):

        r, g, b = pixels[x, y]

        # Nova posição
        new_x = x * 2
        new_y = y * 2

        new_pixels[new_x, new_y] = (r, g, b)

print("Pixels posicionados.")

# Salvar imagem
new_img.save(output_path)

print("Imagem salva em:", output_path)