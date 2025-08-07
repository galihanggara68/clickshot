def init_html(html_path):
    with open(html_path, "w") as f:
        f.write("""<!DOCTYPE html><html><head><meta charset='UTF-8'>
<title>Click Screenshot Log</title>
<style>body{font-family:sans-serif;background:#f4f4f4;padding:20px;}
.step{margin-bottom:30px;background:#fff;padding:15px;border-radius:8px;}
img{max-width:100%;border:1px solid #ccc;margin-top:10px;}
h2[contenteditable],textarea{background:#eef;}textarea{width:100%;padding:8px;margin-top:5px;}</style>
</head><body><button onclick='window.print()'>🖰 Print</button><h1 contenteditable='true'>Click Screenshot Log</h1>
""")

def append_html(html_path, filename, step, timestamp):
    with open(html_path, "a") as f:
        f.write(f"""
<div class='step'>
<h3 contenteditable='true'>Step {step} - {timestamp}</h3>
<h5 contenteditable='true'>Description . . .</h5>
<img src='{filename}' alt='Step {step}'>
</div>
""")

def finalize_html(html_path):
    with open(html_path, "a") as f:
        f.write("</body></html>")