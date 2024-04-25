import tkinter as tk

def renklendir(event):
    text = text_box.get("1.0", "end-1c")
    text_box.tag_remove("unit_renk", "1.0", "end")
    text_box.tag_remove("import_renk", "1.0", "end")
    text_box.tag_remove("gri_renk", "1.0", "end")
    
    start_index = text.find("unit")
    while start_index != -1:
        end_index = start_index + len("unit")
        text_box.tag_add("unit_renk", f"1.0+{start_index}c", f"1.0+{end_index}c")
        text_box.tag_config("unit_renk", foreground="#ADD8E6")
        start_index = text.find("unit", end_index)

    start_index = text.find("import")
    while start_index != -1:
        end_index = start_index + len("import")
        text_box.tag_add("import_renk", f"1.0+{start_index}c", f"1.0+{end_index}c")
        text_box.tag_config("import_renk", foreground="#C284BD")
        start_index = text.find("import", end_index)

    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("!!"):
            text_box.tag_add("gri_renk", f"{i+1}.0", f"{i+1}.end")
            text_box.tag_config("gri_renk", foreground="#689252")
    
    text_box.configure(font=("Helvetica", 12))

root = tk.Tk()
root.title("Metin Kutusu Örneği")

text_box = tk.Text(root, height=20, width=80)
text_box.pack()

text_box.configure(bg="#1F1F1F")

text_box.bind("<KeyRelease>", renklendir)

root.mainloop()
