import os
from rembg import remove

src_dir = r"d:\Wedora\images\3d"

for filename in os.listdir(src_dir):
    if filename.endswith(".png") and not filename.endswith("_nobg.png"):
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(src_dir, filename.replace(".png", "_nobg.png"))
        
        try:
            with open(src_path, "rb") as i_file:
                input_data = i_file.read()
                
            output_data = remove(input_data)
            
            with open(dest_path, "wb") as o_file:
                o_file.write(output_data)
                
            print(f"Removed background for {filename}")
        except Exception as e:
            print(f"Failed {filename}: {e}")
