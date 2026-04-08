# LIR — Logical Image Reconstructor

**LIR (Logical Image Reconstructor)** is an experimental image reconstruction
framework designed to explore alternative interpolation strategies beyond
traditional bilinear methods.

The project focuses on reconstructing higher-resolution images using logical
pixel placement and adaptive interpolation techniques.

---

# 🎯 Objective

Develop and evaluate new image reconstruction techniques based on:

- Logical pixel mapping
- Directional interpolation
- Gradient-based weighting
- Adaptive reconstruction logic

This project is experimental and evolves step-by-step.

---

# 🧩 Reconstruction Pipeline

The LIR system is developed incrementally through structured steps.

## Step Overview

| Step | Name | Description |
|------|------|-------------|
| Step 1 | Pixel Extraction | Load image and access raw pixel data |
| Step 2 | Logical Mapping | Expand image grid to 2× resolution |
| Step 3 | Horizontal Interpolation | Fill horizontal gaps |
| Step 4 | Vertical Interpolation | Fill vertical gaps |
| Step 5 | Bilinear Reconstruction | Complete interpolation pipeline |
| Step 6 | Adaptive Gradient (Full Pixel) | Apply gradient weighting to full RGB pixel |
| Step 7 | Adaptive Gradient (Per Channel) | Apply gradient weighting independently to R, G, B |
| Step 8 | Diagonal Adaptive (Per Channel) | Add diagonal adaptive interpolation and runtime measurement |

---

# 🧠 Key Concepts Explored

- Bilinear interpolation
- Gradient-based interpolation
- Directional dominance
- Channel-level reconstruction
- Adaptive weighting
- Diagonal-aware interpolation
- Runtime performance measurement

---

# 📁 Project Structure
