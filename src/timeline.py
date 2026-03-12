def create_timeline(images_data):
    try:
        dated_images = [img for img in images_data if img["datetime"]]
    except KeyError:
        print("images without datetime!")
        return None
    dated_images.sort(key=lambda x: x["datetime"])

    html = '<div style="position:relative; padding:20px;">'
    html += '<div style="position:absolute; left:50%; width:2px; height:95%; background:#333;"></div>'
    pin_color = ['pink','blue', 'orange', 'green', 'purple',  'brown', 'cadetblue',
                 'black', 'red']
    color_dict = {}
    for img in dated_images:
        dt_obj = img["datetime"].split()[0]
        if dt_obj in color_dict:
            continue
        try:
            color_dict[dt_obj] = pin_color.pop()
        except IndexError:
            color_dict[dt_obj] = "lightgray"
    date_for_check = ""
    num = 0
    for i, img in enumerate(dated_images):
        date_only = img["datetime"].split()[0]
        text_color = color_dict[date_only]
        sides = {0: "right", 1: "left"}
        flex_dirs = {0: "row", 1: "row-reverse"}
        if not date_only == date_for_check: num += 1
        html += f'''
        <div style="margin:20px 0; text-align:{sides[num % 2]}; color: {text_color}; position: relative;">
            <strong>{img["datetime"]}</strong><br>
            {img["filename"]}
        <div style="position:absolute; top:50%; {sides[(num + 1) % 2]}: 50%; display:flex; flex-direction:{flex_dirs[num % 2]}; align-items:center; gap:8px;"><span style="font-family:sans-serif;">{i+1}</span><div style="width:50px; height:2px; background:#333;"></div></div>        <br>
            <small>{img.get("camera_model", "Unknown")}</small>
        </div>'''
        date_for_check = date_only

    html += '</div>'
    return html

