from colorgram import extract

def extract_color(img_dir, color_amt):
    colors = extract(img_dir, color_amt)
    main = []
    final = []
    for color in colors:
        main.append(color.rgb)
    
    for value in main:
        red = value.r
        green = value.g
        blue = value.b
        col = (red, green, blue)
        final.append(col)
    
    return final

