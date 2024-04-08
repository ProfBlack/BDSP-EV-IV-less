import tkinter as tk
import json
import os
import glob
import webbrowser

def reset_evs_or_ev_yields(item, key_name, zero_values):
    if isinstance(item, dict):
        if key_name in item:
            item[key_name] = zero_values
        for key in item:
            reset_evs_or_ev_yields(item[key], key_name, zero_values)
    elif isinstance(item, list):
        for elem in item:
            reset_evs_or_ev_yields(elem, key_name, zero_values)

def process_file(data, key_name):
    zero_values = {'hp': 0, 'atk': 0, 'def': 0, 'spAtk': 0, 'spDef': 0, 'spd': 0}
    reset_evs_or_ev_yields(data, key_name, zero_values)
    return data

def open_hyperlink(url):
    """Open the specified URL in the web browser."""
    webbrowser.open_new(url)

def run_operations(ivs_var, evs_var, ev_yields_var, intro_message, character_label, input_folder, output_folder):
    # Check if no checkboxes are selected
    if not (ivs_var.get() or evs_var.get() or ev_yields_var.get()):
        intro_message.config(state="normal")
        intro_message.delete("1.0", tk.END)
        intro_message.insert(tk.END, "Umm. You actually need to select one or more of the checkboxes for me to be able to do my thing...")
        intro_message.place(relx=0.29, rely=0.55, anchor='center')
        intro_message.config(state="disabled")
        character_label.config(image=beg_image)
        return

    os.makedirs(output_folder, exist_ok=True)
    file_not_found = []

    if ivs_var.get() or evs_var.get():
        file_path = os.path.join(input_folder, 'IOTrainers.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if ivs_var.get():
                    data = process_file(data, 'ivs')
                if evs_var.get():
                    data = process_file(data, 'evs')
            output_file_path = os.path.join(output_folder, 'IOTrainers.json')
            with open(output_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            file_not_found.append('IOTrainers.json')

    if ev_yields_var.get():
        file_path = os.path.join(input_folder, 'IOPokémon.json')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data = process_file(data, 'evYield')
            output_file_path = os.path.join(output_folder, 'IOPokémon.json')
            with open(output_file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            file_not_found.append('IOPokémon.json')

    intro_message.config(state="normal")
    intro_message.delete("1.0", tk.END)
    if len(file_not_found) == 2:
        intro_message.insert(tk.END, "Double drat! Both IOTrainers.json and IOPokémon.json files are missing.")
        intro_message.place(relx=0.29, rely=0.55, anchor='center')
        character_label.config(image=drat_image)
    elif file_not_found:
        intro_message.insert(tk.END, f"Drat. {', '.join(file_not_found)} file{'s' if len(file_not_found) > 1 else ''} not found.")
        intro_message.place(relx=0.29, rely=0.55, anchor='center')
        character_label.config(image=drat_image)
    else:
        intro_message.insert(tk.END, "Success! \nAll operations have been completed. \nNow all ya gotta do is grab your new files from the Output folder and import them with Imposter's Ordeal, then save your new mod! \nBest of luck!")
        intro_message.place(relx=0.29, rely=0.4, anchor='center')
        character_label.config(image=happy_image)
    intro_message.config(state="disabled")

def create_gui():
    root = tk.Tk()
    root.title("EV/IV-less")

    if os.name == 'nt':
        root.iconbitmap("_assets/icon.ico")
    else:
        icon_image = tk.PhotoImage(file="_assets/icon.ico")
        root.iconphoto(True, icon_image)

    global happy_image, drat_image, beg_image
    happy_image = tk.PhotoImage(file="_assets/happy.png")
    drat_image = tk.PhotoImage(file="_assets/drat.png")
    beg_image = tk.PhotoImage(file="_assets/beg.png")

    canvas = tk.Canvas(root, height=400, width=600)
    canvas.pack()

    character_image = tk.PhotoImage(file="_assets/rested.png")
    character_label = tk.Label(root, image=character_image)
    character_label.image = character_image
    character_label.place(relx=0.75, rely=0.475, anchor='center')

    intro_message = tk.Text(root, height=10, width=42, wrap=tk.WORD, bg=root.cget("bg"), borderwidth=0, font=("TkDefaultFont", 10))
    intro_message.insert(tk.END, "Hi there, I'm Dev DJ!\n\nHere to help you out with your EVs and IVs.\n\nMake sure that you have IOTrainers.json and IOPokémon.json exported from ")
    intro_message.insert(tk.END, "Imposter's Ordeal", "hyperlink")
    intro_message.insert(tk.END, " in the Input folder. Then tick the boxes as you like and press ")
    intro_message.insert(tk.END, "Go!", "bold")
    intro_message.tag_configure("hyperlink", foreground="blue", underline=1)
    intro_message.tag_bind("hyperlink", "<Button-1>", lambda e: open_hyperlink("https://github.com/Nifyr/Imposters-Ordeal"))
    intro_message.tag_configure("bold", font=("TkDefaultFont", 10, "bold"))
    intro_message.configure(state="disabled", cursor="arrow")
    intro_message.place(relx=0.29, rely=0.4, anchor='center')

    ivs_var = tk.BooleanVar()
    evs_var = tk.BooleanVar()
    ev_yields_var = tk.BooleanVar()

    tk.Checkbutton(root, text="Reset Trainer IVs", variable=ivs_var).place(relx=0.25, rely=0.6, anchor='center')
    tk.Checkbutton(root, text="Reset Trainer EVs", variable=evs_var).place(relx=0.25, rely=0.65, anchor='center')
    tk.Checkbutton(root, text="Reset EV Yields", variable=ev_yields_var).place(relx=0.25, rely=0.7, anchor='center')

    input_folder = os.path.join('Input')
    output_folder = os.path.join('Output')

    run_button = tk.Button(root, text=" Go! ", command=lambda: run_operations(ivs_var, evs_var, ev_yields_var, intro_message, character_label, input_folder, output_folder))
    run_button.place(relx=0.25, rely=0.8, anchor='center')

    root.mainloop()

if __name__ == "__main__":
    create_gui()
