import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import threading

# ---------- Pixel manipulation ----------
def xor_image(img, key):
    """Return a new image where each pixel's R,G,B bytes are XOR'd with key."""
    img = img.convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
    return img


# ---------- Main App ----------
class PixelEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Pixel Image Encryption Tool v2")
        self.root.geometry("900x600")
        self.root.configure(bg="#f2f4f7")

        self.image_path = None
        self.original_img = None
        self.processed_img = None
        self.tk_original = None
        self.tk_processed = None

        self.build_ui()

    # ---------- UI Layout ----------
    def build_ui(self):
        title = tk.Label(
            self.root,
            text="Pixel Manipulation — Image Encryption Tool",
            font=("Segoe UI", 18, "bold"),
            bg="#f2f4f7",
            fg="#333"
        )
        title.pack(pady=15)

        frame = tk.Frame(self.root, bg="#f2f4f7")
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Left side: Original image
        self.left_panel = tk.LabelFrame(frame, text="Original Image", bg="#f2f4f7", font=("Segoe UI", 11, "bold"))
        self.left_panel.pack(side="left", padx=20, pady=10)
        self.original_label = tk.Label(self.left_panel, bg="#ddd", width=45, height=18, relief="ridge")
        self.original_label.pack(padx=10, pady=10)

        # Right side: Processed image
        self.right_panel = tk.LabelFrame(frame, text="Encrypted / Decrypted Image", bg="#f2f4f7", font=("Segoe UI", 11, "bold"))
        self.right_panel.pack(side="right", padx=20, pady=10)
        self.processed_label = tk.Label(self.right_panel, bg="#ddd", width=45, height=18, relief="ridge")
        self.processed_label.pack(padx=10, pady=10)

        # Bottom control frame
        controls = tk.Frame(self.root, bg="#f2f4f7")
        controls.pack(pady=15)

        tk.Button(controls, text="📂 Select Image", font=("Segoe UI", 10, "bold"), command=self.select_image).grid(row=0, column=0, padx=10)

        tk.Label(controls, text="Key (0–255):", bg="#f2f4f7", font=("Segoe UI", 10)).grid(row=0, column=1, padx=5)
        self.key_entry = tk.Entry(controls, width=6, justify="center")
        self.key_entry.insert(0, "42")
        self.key_entry.grid(row=0, column=2, padx=5)

        tk.Button(controls, text="🔒 Encrypt", bg="#c6e2b3", width=10, command=self.encrypt_image).grid(row=0, column=3, padx=10)
        tk.Button(controls, text="🔓 Decrypt", bg="#f8d7da", width=10, command=self.decrypt_image).grid(row=0, column=4, padx=10)
        tk.Button(controls, text="💾 Save Image", bg="#b3d7e2", width=12, command=self.save_image).grid(row=0, column=5, padx=10)
        tk.Button(controls, text="♻️ Reset", bg="#e2e2e2", width=10, command=self.reset).grid(row=0, column=6, padx=10)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", mode="determinate", length=600)
        self.progress.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="Select an image to begin.", font=("Segoe UI", 10), bg="#f2f4f7", fg="#555")
        self.status_label.pack()

    # ---------- Utility ----------
    def select_image(self):
        path = filedialog.askopenfilename(
            title="Select an image file",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            self.original_img = Image.open(path)
            self.image_path = path
            self.show_image(self.original_img, self.original_label)
            self.status_label.config(text=f"Loaded: {os.path.basename(path)} | Size: {self.original_img.size}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image:\n{e}")

    def show_image(self, img, label):
        img_copy = img.copy()
        img_copy.thumbnail((350, 350))
        tk_img = ImageTk.PhotoImage(img_copy)
        label.config(image=tk_img)
        label.image = tk_img

    def get_key(self):
        try:
            key = int(self.key_entry.get())
            if 0 <= key <= 255:
                return key
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Key", "Please enter a valid key between 0–255.")
            return None

    def process_image(self, mode):
        if not self.original_img:
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        key = self.get_key()
        if key is None:
            return

        self.status_label.config(text=f"Processing {mode}...")
        self.progress.start(10)

        def task():
            try:
                self.processed_img = xor_image(self.original_img, key)
                self.show_image(self.processed_img, self.processed_label)
                self.status_label.config(text=f"{mode.capitalize()} completed successfully (key={key})")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                self.progress.stop()

        threading.Thread(target=task).start()

    def encrypt_image(self):
        self.process_image("encryption")

    def decrypt_image(self):
        self.process_image("decryption")

    def save_image(self):
        if not self.processed_img:
            messagebox.showinfo("No Image", "There’s no processed image to save.")
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("All Files", "*.*")]
        )
        if not path:
            return
        try:
            self.processed_img.save(path)
            messagebox.showinfo("Saved", f"Image saved successfully:\n{path}")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))

    def reset(self):
        self.image_path = None
        self.original_img = None
        self.processed_img = None
        self.original_label.config(image="", text="")
        self.processed_label.config(image="", text="")
        self.status_label.config(text="Select an image to begin.")
        self.progress.stop()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, "42")


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = PixelEncryptorApp(root)
    root.mainloop()
