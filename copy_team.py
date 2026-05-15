import os
import shutil
from PIL import Image

def process():
    src1 = r"C:\Users\karti\.gemini\antigravity\brain\34b3f08c-4fc5-4841-a595-b285f9bc5ac6\media__1778757305108.jpg"
    src2 = r"C:\Users\karti\.gemini\antigravity\brain\34b3f08c-4fc5-4841-a595-b285f9bc5ac6\media__1778757465621.jpg"
    
    out_dir = r"d:\Wedora\images\team"
    os.makedirs(out_dir, exist_ok=True)
    
    # Process Divyansh
    img1 = Image.open(src1)
    if img1.mode in ("RGBA", "P"): img1 = img1.convert("RGB")
    ratio = min(800/img1.width, 1000/img1.height)
    if ratio < 1: img1 = img1.resize((int(img1.width*ratio), int(img1.height*ratio)), Image.Resampling.LANCZOS)
    img1.save(os.path.join(out_dir, "divyansh.jpg"), "JPEG", quality=85)
    
    # Process Kamlesh
    img2 = Image.open(src2)
    if img2.mode in ("RGBA", "P"): img2 = img2.convert("RGB")
    ratio = min(800/img2.width, 1000/img2.height)
    if ratio < 1: img2 = img2.resize((int(img2.width*ratio), int(img2.height*ratio)), Image.Resampling.LANCZOS)
    img2.save(os.path.join(out_dir, "kamlesh.jpg"), "JPEG", quality=85)

if __name__ == "__main__":
    process()
