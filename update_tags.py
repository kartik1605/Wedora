import json
from bs4 import BeautifulSoup

html_file = r"d:\Wedora\gallery.html"
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

taglines = {
    "carnival": [
        ("The Grand Carnival", "Vibrant entrance & decor"),
        ("Joyous Festivities", "Colorful canopies in motion"),
        ("Radiant Celebrations", "A kaleidoscope of colors")
    ],
    "petals": [
        ("Enchanted Walkway", "A path of blooming lilacs"),
        ("The Floral Arch", "Elegance in every petal"),
        ("Twilight Ambience", "Soft glows & purple hues"),
        ("Regal Centerpieces", "Ornate silver and blooms"),
        ("The Mandap Decor", "A symphony of pastels"),
        ("Lilac Dreams", "Where romance blossoms")
    ],
    "sage": [
        ("Botanical Elegance", "Lush green pathways"),
        ("Earthy Textures", "A natural, grounded setup"),
        ("The Verdant Canopy", "Under the leaves"),
        ("Serene Ambiance", "Soft light & green hues"),
        ("Floral & Foliage", "The perfect natural blend"),
        ("The Enchanted Forest", "A magical green setting"),
        ("Rustic Charm", "Woodlands & elegance"),
        ("Sage Symphony", "Nature's grand stage")
    ],
    "yellow": [
        ("Golden Marigolds", "The essence of Haldi"),
        ("Sunny Celebrations", "Bright & joyful ambiance"),
        ("The Yellow Canopy", "Warmth in every drape"),
        ("Vibrant Centerpieces", "Sunflowers and smiles"),
        ("Golden Hour Glow", "A radiant setup"),
        ("The Haldi Stage", "Where memories are made"),
        ("Floral Abundance", "Cascading yellow blooms"),
        ("Warm Festivities", "An inviting glow"),
        ("The Grand Arch", "A golden entrance"),
        ("Yellow Botanica", "Sunshine and love")
    ],
    "crimson": [
        ("Luxurious Red Roses", "A romantic floral spread"),
        ("The Regal Stage", "Deep crimson & gold"),
        ("Dramatic Ambiance", "A night of elegance"),
        ("Crimson Centerpiece", "Ornate golden vases"),
        ("The Grand Setup", "A luxurious aura")
    ],
    "casino": [
        ("The High Rollers", "Glamorous casino tables"),
        ("Neon Nights", "Sparkling Sangeet energy"),
        ("The Poker Setup", "Cards, chips, and fun"),
        ("Royal Ambiance", "A golden casino floor"),
        ("The Winning Hand", "A night of celebration")
    ]
}

sections = soup.find_all("section", class_="catalogue-section")
for sec in sections:
    cat = sec.get("data-catalogue")
    if cat in taglines:
        items = sec.find_all("div", class_="slide-item")
        for i, item in enumerate(items):
            if i < len(taglines[cat]):
                label, sub = taglines[cat][i]
                
                # update data attrs
                item["data-label"] = label
                item["data-sub"] = sub
                
                # update spans
                overlay = item.find("div", class_="slide-overlay")
                if overlay:
                    span_label = overlay.find("span", class_="slide-label")
                    if span_label:
                        span_label.string = label
                        
                    span_sub = overlay.find("span", class_="slide-sub")
                    if span_sub:
                        span_sub.string = sub

with open(html_file, "w", encoding="utf-8") as f:
    f.write(str(soup))
print("Gallery taglines updated successfully!")
