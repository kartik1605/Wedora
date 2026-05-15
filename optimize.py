import os
from PIL import Image

src_dir = r"d:\Wedora\images\downloads"
dest_dir = r"d:\Wedora\images\optimized"

folders_to_optimize = [
    "Crimson Aura",
    "Royal Casino Sangeet"
]

for folder in folders_to_optimize:
    src_folder = os.path.join(src_dir, folder)
    dest_folder = os.path.join(dest_dir, folder)
    os.makedirs(dest_folder, exist_ok=True)
    
    for filename in os.listdir(src_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            src_path = os.path.join(src_folder, filename)
            dest_filename = os.path.splitext(filename)[0] + '.jpg'
            dest_path = os.path.join(dest_folder, dest_filename)
            
            try:
                with Image.open(src_path) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    # Resize if too large
                    max_size = (1200, 1200)
                    img.thumbnail(max_size, Image.Resampling.LANCZOS)
                    img.save(dest_path, "JPEG", quality=85, optimize=True)
                print(f"Optimized: {dest_path}")
            except Exception as e:
                print(f"Failed to optimize {src_path}: {e}")
