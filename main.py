import tkinter as tk
from datetime import date, datetime
from tkinter import messagebox
import os

desktop = r'C:\Users\devdu\OneDrive\Tài liệu\git\AnHoaiKhongLon.github.io\_posts'
# Function to save the input data
def save_data():
    tittle = title_entry.get()
    id = id_entry.get()
    date = date_entry.get()
    time = time_entry.get()
    content = content_entry.get("1.0", "end-1c")  # Get content from Text widget

    # You can process or store the data as needed
    data = f"Title: {tittle}\nDate: {date}\nTime: {time}\nContent: {content}"

    messagebox.showinfo("Data Saved", data)

    if tittle == "":
        tittle = content.split("\n")[0]        
    content = content.replace("\n", "\n\n")
    # Tạo file
    linh = """---
    # multilingual page pair id, this must pair with translations of this page. (This name must be unique)
    lng_pair: " """ + tittle + """ "
    title: " """ + tittle + """ "
    # post specific
    # if not specified, .name will be used from _data/owner/[language].yml
    #author: Xíu
    # multiple category is not supported
    category: Facebook
    # multiple tag entries are possible
    tags: [Facebook]
    # thumbnail image for post
    img: "https://xiungo.github.io/img/""" + id + """.jpg"
    # disable comments on this page
    #comments_disable: false
    # publish date
    date: """ + date + """ """ + time + """ +0900
    # seo
    # if not specified, date will be used.
    #meta_modify_date: """ + date + """ """ + time + """ +0900
    # check the meta_common_description in _data/owner/[language].yml
    #meta_description: ""
    # optional
    # if you enabled image_viewer_posts you don't need to enable this. This is only if image_viewer_posts = false
    #image_viewer_on: true
    # if you enabled image_lazy_loader_posts you don't need to enable this. This is only if image_lazy_loader_posts = false
    #image_lazy_loader_on: true
    # exclude from on site search
    #on_site_search_exclude: true
    # exclude from search engines
    #search_engine_exclude: true
    # to disable this page, simply set published: false or delete this file
    #published: false
    ---
    """+content+"""
    <!-- outline-end -->
    <img src= "https://xiungo.github.io/img/"""+id + """.jpg">"""

    # ghi file
    filename = os.path.join(desktop, date + "-"+id+".markdown")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(linh)
        
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Movie Information")

# Title input
title_label = tk.Label(root, text="Title:")
title_label.pack()
title_entry = tk.Entry(root)
title_entry.pack()

# Id input
id_label = tk.Label(root, text="Id:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# Date input
date_label = tk.Label(root, text="Date (yyyy-mm-dd):")
date_label.pack()
date = date.today().strftime('%Y-%m-%d')  # Default to today's date
date_entry = tk.Entry(root)
date_entry.insert(0, date)
date_entry.pack()

# Time input
time_label = tk.Label(root, text="Time (hh:mm:ss 24h):")
time_label.pack()
current_time = datetime.now().strftime('%H:%M:%S')  # Default to current time
time_entry = tk.Entry(root)
time_entry.insert(0, current_time)
time_entry.pack()

# Content input
content_label = tk.Label(root, text="Content:")
content_label.pack()
content_entry = tk.Text(root, height=5, width=30)
content_entry.pack()

# Save button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack()

root.mainloop()

