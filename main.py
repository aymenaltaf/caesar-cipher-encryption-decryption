import os
import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

# ==========================================
# Caesar Cipher Functions
# ==========================================

def encrypt(text, shift):
    result = ""

    for char in text:

        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - base + shift) % 26 + base)

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)

# ==========================================
# Encrypt Button
# ==========================================

def encrypt_text():

    message = message_box.get("1.0", tk.END).strip()

    if message == "":
        status.config(
            text="⚠ Please enter a message.",
            bootstyle="danger"
        )
        return

    try:
        shift = int(shift_entry.get())

        if shift < 1 or shift > 25:
            status.config(
                text="⚠ Shift key must be between 1 and 25.",
                bootstyle="danger"
            )
            return

    except ValueError:
        status.config(
            text="⚠ Shift key must be a number.",
            bootstyle="danger"
        )
        return

    encrypted = encrypt(message, shift)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, encrypted)

    status.config(
        text="🔒 Encryption Successful",
        bootstyle="success"
    )


# ==========================================
# Decrypt Button
# ==========================================

def decrypt_text():

    message = message_box.get("1.0", tk.END).strip()

    if message == "":
        status.config(
            text="⚠ Please enter encrypted text.",
            bootstyle="danger"
        )
        return

    try:
        shift = int(shift_entry.get())

        if shift < 1 or shift > 25:
            status.config(
                text="⚠ Shift key must be between 1 and 25.",
                bootstyle="danger"
            )
            return

    except ValueError:
        status.config(
            text="⚠ Shift key must be a number.",
            bootstyle="danger"
        )
        return

    decrypted = decrypt(message, shift)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, decrypted)

    status.config(
        text="🔓 Decryption Successful",
        bootstyle="info"
    )


# ==========================================
# Clear Button
# ==========================================

def clear_text():

    message_box.delete("1.0", tk.END)
    result_box.delete("1.0", tk.END)

    shift_entry.delete(0, tk.END)
    shift_entry.insert(0, "3")

    status.config(
        text="🧹 Cleared Successfully",
        bootstyle="warning"
    )


# ==========================================
# Copy Button
# ==========================================

def copy_result():

    result = result_box.get("1.0", tk.END).strip()

    if result == "":
        status.config(
            text="⚠ Nothing to copy.",
            bootstyle="warning"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(result)

    status.config(
        text="📋 Result copied to clipboard.",
        bootstyle="success"
    )
# ==========================================
# About Function
# ==========================================

def show_about():

    tb.dialogs.Messagebox.show_info(
        title="About",
        message=(
            "Caesar Cipher Encryption & Decryption Tool\n\n"
            "Developed by Aymen Altaf\n\n"
            "Version 1.0"
        )
    )
# ==========================================
# Create Window
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "logo.png")

root = tb.Window(themename="darkly")
root.title("Caesar Cipher Encryption & Decryption Tool")
root.geometry("760x670")
root.resizable(False, False)

icon_path = os.path.join(BASE_DIR, "icon.ico")

if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

# ==========================================
# Load Logo
# ==========================================

if os.path.exists(logo_path):

    logo = Image.open(logo_path)
    logo = logo.resize((100, 100))

    logo_img = ImageTk.PhotoImage(logo)

    logo_label = tb.Label(root, image=logo_img)
    logo_label.image = logo_img
    logo_label.pack(pady=(10, 5))

# ==========================================
# Title
# ==========================================

tb.Label(
    root,
    text="Caesar Cipher Encryption & Decryption Tool",
    font=("Segoe UI", 20, "bold"),
    bootstyle="light"
).pack(pady=10)

# ==========================================
# Message Input
# ==========================================

frame1 = tb.Frame(root)
frame1.pack(fill=X, padx=20, pady=10)

tb.Label(
    frame1,
    text="Enter Message",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w")

message_box = tk.Text(
    frame1,
    height=6,
    font=("Consolas", 11)
)

message_box.pack(fill=X)

# ==========================================
# Shift Key
# ==========================================

frame2 = tb.Frame(root)
frame2.pack(fill=X, padx=20, pady=10)

tb.Label(
    frame2,
    text="Shift Key",
    font=("Segoe UI", 11, "bold")
).pack(side=LEFT)

shift_entry = tb.Entry(
    frame2,
    width=8,
    justify="center"
)

shift_entry.insert(0, "3")
shift_entry.pack(side=LEFT, padx=10)

# ==========================================
# Buttons Frame
# ==========================================

button_frame = tb.Frame(root)
button_frame.pack(pady=20)

encrypt_btn = tb.Button(
    button_frame,
    text="Encrypt",
    width=12,
    bootstyle="success",
    command=encrypt_text
)

decrypt_btn = tb.Button(
    button_frame,
    text="Decrypt",
    width=12,
    bootstyle="primary",
    command=decrypt_text
)

copy_btn = tb.Button(
    button_frame,
    text="Copy",
    width=12,
    bootstyle="info",
    command=copy_result
)

clear_btn = tb.Button(
    button_frame,
    text="Clear",
    width=12,
    bootstyle="danger",
    command=clear_text
)
exit_btn = tb.Button(
    button_frame,
    text="Exit",
    width=12,
    bootstyle="secondary",
    command=root.destroy
)
about_btn = tb.Button(
    button_frame,
    text="About",
    width=12,
    bootstyle="warning",
    command=show_about
)
encrypt_btn.pack(side=LEFT, padx=6)
decrypt_btn.pack(side=LEFT, padx=6)
copy_btn.pack(side=LEFT, padx=6)
clear_btn.pack(side=LEFT, padx=6)
exit_btn.pack(side=LEFT, padx=6)
about_btn.pack(side=LEFT, padx=6)


# ==========================================
# Result
# ==========================================

frame3 = tb.Frame(root)
frame3.pack(fill=BOTH, expand=True, padx=20)

tb.Label(
    frame3,
    text="Result",
    font=("Segoe UI", 11, "bold")
).pack(anchor="w")

result_box = tk.Text(
    frame3,
    height=8,
    font=("Consolas", 11)
)

result_box.pack(fill=BOTH, expand=True)

# ==========================================
# Status Bar
# ==========================================

status = tb.Label(
    root,
    text="🟢 Ready",
    anchor="w",
    bootstyle="inverse-success"
)

status.pack(fill=X, side=BOTTOM)
footer = tb.Label(
    root,
    text="Developed by Aymen Altaf ",
    font=("Segoe UI", 9),
    anchor="center",
    bootstyle="secondary"
)

footer.pack(side=BOTTOM, pady=5)

# ==========================================
# Keyboard Shortcuts
# ==========================================

# Press Enter to Encrypt
root.bind("<Return>", lambda event: encrypt_text())

# Ctrl + L to Clear
root.bind("<Control-l>", lambda event: clear_text())

# Ctrl + C to Copy Result
root.bind("<Control-c>", lambda event: copy_result())

message_box.focus()

root.mainloop()