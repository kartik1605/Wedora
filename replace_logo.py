import os
import re

html_files = [f for f in os.listdir(r"d:\Wedora") if f.endswith('.html')]

for file in html_files:
    filepath = os.path.join(r"d:\Wedora", file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace canvases
    content = re.sub(
        r'<canvas\s+id="loaderCanvas"[^>]*class="loader-logo"[^>]*></canvas>',
        r'<img src="images/logo.png" alt="Wedora Logo" class="loader-logo" style="width: 100px; height: auto;" />',
        content
    )
    
    content = re.sub(
        r'<canvas\s+id="navCanvas"[^>]*></canvas>',
        r'<img src="images/logo.png" alt="Wedora Logo" style="height: 52px; width: auto;" />',
        content
    )
    
    content = re.sub(
        r'<canvas\s+id="footerCanvas"[^>]*></canvas>',
        r'<img src="images/logo.png" alt="Wedora Logo" style="height: 72px; width: auto; margin-bottom: 16px; display: block;" />',
        content
    )

    # Remove Javascript that drew the canvas
    # For index.html
    if file == 'index.html':
        content = re.sub(
            r'function drawLogo.*?drawLogo\(document\.getElementById\(\'footerCanvas\'\), 30\);',
            '',
            content,
            flags=re.DOTALL
        )
    else:
        # For other files
        content = re.sub(
            r'const ctx = document\.getElementById\(\'navCanvas\'\)\.getContext\(\'2d\'\);\s*ctx\.fillStyle.*?ctx\.fillText\(\'Wedora\', 6, 34\);',
            '',
            content,
            flags=re.DOTALL
        )
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete.")
