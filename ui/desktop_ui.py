import tkinter as tk

def launch_ui():
    root = tk.Tk()
    root.title("JARVIS")
    root.geometry("800x500")
    root.configure(bg="black")

    label = tk.Label(
        root,
        text="JARVIS ONLINE",
        fg="cyan",
        bg="black",
        font=("Orbitron", 28)
    )
    label.pack(pady=40)

    root.mainloop()

