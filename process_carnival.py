import os
from PIL import Image
import imagehash

def process_images():
    src_dir = r"d:\Wedora\Carnival Reverie"
    dest_dir = r"d:\Wedora\images\optimized\Carnival Reverie"
    
    # Get hashes of existing images
    existing_hashes = []
    for f in os.listdir(dest_dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                img_path = os.path.join(dest_dir, f)
                img = Image.open(img_path)
                h = imagehash.phash(img)
                existing_hashes.append(h)
                print(f"Existing {f} hash: {h}")
            except Exception as e:
                print(f"Error reading {f}: {e}")
                
    # Find next available index for naming
    existing_files = [f for f in os.listdir(dest_dir) if f.lower().endswith('.jpg')]
    existing_indices = []
    for f in existing_files:
        try:
            existing_indices.append(int(os.path.splitext(f)[0]))
        except:
            pass
    next_idx = max(existing_indices) + 1 if existing_indices else 1
    
    new_files = []
    
    # Process new images
    for f in sorted(os.listdir(src_dir)):
        if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(src_dir, f)
            try:
                img = Image.open(img_path)
                h = imagehash.phash(img)
                
                # Check for duplicates (hamming distance < 5 is usually a duplicate)
                is_duplicate = False
                for ex_h in existing_hashes:
                    if h - ex_h < 5:
                        is_duplicate = True
                        break
                        
                if is_duplicate:
                    print(f"Skipping {f} - Duplicate found")
                else:
                    print(f"Adding new image {f} with hash {h}")
                    existing_hashes.append(h)
                    
                    # Convert and optimize
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Resize if too large
                    max_dim = 1200
                    if img.width > max_dim or img.height > max_dim:
                        ratio = min(max_dim/img.width, max_dim/img.height)
                        new_size = (int(img.width * ratio), int(img.height * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                        
                    out_name = f"{next_idx}.jpg"
                    out_path = os.path.join(dest_dir, out_name)
                    img.save(out_path, "JPEG", quality=85, optimize=True)
                    new_files.append(out_path)
                    next_idx += 1
            except Exception as e:
                print(f"Error processing {f}: {e}")
                
    print(f"Added {len(new_files)} new images.")
    return new_files

if __name__ == "__main__":
    process_images()
