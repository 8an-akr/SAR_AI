#!/usr/bin/env python3
import kagglehub

# Download latest version
path = kagglehub.dataset_download("requiemonk/sentinel12-image-pairs-segregated-by-terrain")

print("Path to dataset files:", path)