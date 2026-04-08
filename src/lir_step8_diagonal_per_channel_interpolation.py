# ==========================================================
# LIR Step 8 — Diagonal Adaptive RGB Interpolation
#
# Extends Step7 by adding diagonal adaptive reconstruction
# using four-neighbor directional analysis.
#
# Pipeline:
# Step1 — Original pixel mapping
# Step2 — Horizontal adaptive interpolation
# Step3 — Vertical adaptive interpolation
# Step4 — Diagonal adaptive interpolation
#
# Each RGB channel independently selects
# the most consistent diagonal based on
# gradient comparison.
#
# Performance instrumentation:
# Execution time measurement using
# high-precision performance counter.
#
# Purpose:
# Improve diagonal edge reconstruction
# and provide measurable computational
# performance data for algorithm analysis.
#
# Key concepts introduced:
# - Per-channel diagonal gradient selection
# - Runtime performance measurement
# ==========================================================

from PIL import Image
import time

# ============================
# INÍCIO DO CRONÔMETRO
# ============================

start_time = time.perf_counter()

# ============================
# CONFIGURAÇÃO EXPERIMENTAL
# ============================

THRESHOLD = 50

WEIGHT_DOMINANT = 0.8
WEIGHT_WEAK = 0.2

WEIGHT_NORMAL = 0.5


# ============================
# FUNÇÕES BASE (STEP7)
# ============================

def adaptive_channel(v1, v3):

    diff = v3 - v1

    if diff > THRESHOLD:

        return int(
            v1 * WEIGHT_WEAK +
            v3 * WEIGHT_DOMINANT
        )

    elif diff < -THRESHOLD:

        return int(
            v1 * WEIGHT_DOMINANT +
            v3 * WEIGHT_WEAK
        )

    else:

        return int(
            v1 * WEIGHT_NORMAL +
            v3 * WEIGHT_NORMAL
        )


def channel_adaptive_pixel(p1, p3):

    r = adaptive_channel(p1[0], p3[0])
    g = adaptive_channel(p1[1], p3[1])
    b = adaptive_channel(p1[2], p3[2])

    return (r, g, b)


# ============================
# FUNÇÕES NOVAS (STEP8)
# ============================

def diagonal_channel(a, b, c, d):

    diff_AD = abs(a - d)
    diff_BC = abs(b - c)

    if diff_AD < diff_BC:

        return adaptive_channel(a, d)

    else:

        return adaptive_channel(b, c)


def adaptive_diagonal_pixel(A, B, C, D):

    r = diagonal_channel(
        A[0], B[0], C[0], D[0]
    )

    g = diagonal_channel(
        A[1], B[1], C[1], D[1]
    )

    b = diagonal_channel(
        A[2], B[2], C[2], D[2]
    )

    return (r, g, b)


# ============================
# CAMINHOS
# ============================

input_path = "../input/input.png"
output_path = "../output/output_step8_diagonal_adaptive.png"


# ============================
# ABRIR IMAGEM
# ============================

img = Image.open(input_path).convert("RGB")

width, height = img.size
pixels = img.load()


# ============================
# CRIAR NOVA IMAGEM 2x
# ============================

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

        new_pixels[x * 2, y * 2] = pixels[x, y]


# ----------------------------
# PASSO 2 — Horizontal
# ----------------------------

for y in range(0, new_height, 2):
    for x in range(1, new_width - 1, 2):

        left = new_pixels[x - 1, y]
        right = new_pixels[x + 1, y]

        new_pixels[x, y] = channel_adaptive_pixel(
            left,
            right
        )


# ----------------------------
# PASSO 3 — Vertical
# ----------------------------

for y in range(1, new_height - 1, 2):
    for x in range(0, new_width, 2):

        top = new_pixels[x, y - 1]
        bottom = new_pixels[x, y + 1]

        new_pixels[x, y] = channel_adaptive_pixel(
            top,
            bottom
        )


# ----------------------------
# PASSO 4 — Diagonal
# ----------------------------

for y in range(1, new_height - 1, 2):

    for x in range(1, new_width - 1, 2):

        A = new_pixels[x - 1, y - 1]
        B = new_pixels[x + 1, y - 1]
        C = new_pixels[x - 1, y + 1]
        D = new_pixels[x + 1, y + 1]

        new_pixels[x, y] = adaptive_diagonal_pixel(
            A, B, C, D
        )


# ============================
# SALVAR RESULTADO
# ============================

new_img.save(output_path)

# ============================
# FIM DO CRONÔMETRO
# ============================

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Step8 completo — interpolação diagonal aplicada.")
print("Imagem salva em:", output_path)

print(f"Tempo de execução: {elapsed_time:.6f} segundos")