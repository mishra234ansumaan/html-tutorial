import tkinter as tk

# Define color schemes for light and dark themes
LIGHT = {'bg': 'white', 'fg': 'black', 'btn_bg': '#f0f0f0', 'btn_fg': 'black'}
DARK = {'bg': '#252526', 'fg': 'white', 'btn_bg': '#333333', 'btn_fg': 'white'}

class ModernCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Calculator")
        self.geometry("340x410")
        self.resizable(False, False)
        self.theme = LIGHT
        self.expression = ''
        self._setup_ui()

    def _setup_ui(self):
        # Display
        self.display = tk.Entry(self, font=("Segoe UI", 22), border=0, relief=tk.FLAT, justify="right")
        self.display.pack(fill="both", padx=15, pady=15, ipady=10)
        
        # Theme switch button on the left
        self.theme_btn = tk.Button(self, text="🌙", font=("Segoe UI", 14), command=self._toggle_theme, border=0)
        self.theme_btn.place(relx=0.0, rely=0.03, anchor="nw")
        
        # Buttons grid
        btns = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', 'C', '=', '+']
        ]
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10)
        for r, row in enumerate(btns):
            for c, label in enumerate(row):
                b = tk.Button(frame, text=label, font=("Segoe UI", 18),
                              command=lambda x=label: self._press(x),
                              border=0, width=4, height=2)
                b.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        self._apply_theme()

        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)

    def _apply_theme(self):
        colors = self.theme
        self.configure(bg=colors['bg'])
        self.display.config(bg=colors['bg'], fg=colors['fg'], insertbackground=colors['fg'])
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=colors['btn_bg'], fg=colors['btn_fg'], activebackground=colors['btn_bg'], activeforeground=colors['btn_fg'])
        self.display.config(bg=colors['bg'], fg=colors['fg'])
        self.theme_btn.config(text="🌙" if self.theme == LIGHT else "☀")

    def _toggle_theme(self):
        self.theme = DARK if self.theme == LIGHT else LIGHT
        self._apply_theme()

    def _press(self, key):
        if key == 'C':
            self.expression = ''
        elif key == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = 'Error'
        else:
            self.expression += key
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    ModernCalculator().mainloop()
