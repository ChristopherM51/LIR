# LIR Step History

## Step 1 — Pixel Extraction
Load image and enable direct pixel access.

## Step 2 — Logical Mapping
Expand image grid to 2× resolution.

## Step 3 — Horizontal Interpolation
Fill horizontal gaps using linear interpolation.

## Step 4 — Vertical Interpolation
Fill vertical gaps using linear interpolation.

## Step 5 — Bilinear Reconstruction
Combine horizontal and vertical reconstruction.

## Step 6 — Adaptive Gradient (Full Pixel)
Introduce gradient-based weighting applied to full RGB pixel.

## Step 7 — Adaptive Gradient (Per Channel)
Apply adaptive gradient logic independently to each RGB channel.

## Step 8 — Diagonal Adaptive (Per Channel)
Introduce diagonal interpolation using four-neighbor analysis.

Each missing diagonal pixel is reconstructed by evaluating both
possible diagonals and selecting the one with the smallest
gradient difference independently per RGB channel.

Also introduces execution time measurement to monitor
computational cost during reconstruction.

Key additions:
- Diagonal gradient comparison (A↔D vs B↔C)
- Per-channel diagonal selection
- Adaptive diagonal reconstruction
- Runtime execution timer