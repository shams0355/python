import tkinter as tk
from tkinter import messagebox
import json
import os
import re


class DarazApp:
    def __init__(self, root):
        self.root = root

        # ---------------- WINDOW SETTINGS ----------------
        self.root.title("DARAZ.PK - Account")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # ---------------- ACCOUNT DATA ----------------
        self.login_accounts_info = {}
        self.current_user = None
        self.current_name = None

        self.load_accounts()

        # ---------------- COLORS ----------------
        self.orange = "#f85606"
        self.dark_orange = "#d94700"
        self.light_orange = "#fff1e8"
        self.white = "#ffffff"
        self.dark = "#333333"
        self.gray = "#777777"
        self.light_gray = "#eeeeee"
        self.green = "#28a745"
        self.red = "#dc3545"

        self.show_welcome()


    # =====================================================
    # FILE HANDLING
    # =====================================================

    def load_accounts(self):
        """Load saved accounts from JSON file."""

        if os.path.exists("daraz_accounts.json"):

            try:
                with open("daraz_accounts.json", "r") as file:
                    self.login_accounts_info = json.load(file)

            except:
                self.login_accounts_info = {}

        else:
            self.login_accounts_info = {}


    def save_accounts(self):
        """Save accounts to JSON file."""

        with open("daraz_accounts.json", "w") as file:
            json.dump(self.login_accounts_info, file, indent=4)


    # =====================================================
    # GENERAL GUI FUNCTIONS
    # =====================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    def create_title(self, parent, text, size=28):

        title = tk.Label(
            parent,
            text=text,
            font=("Arial", size, "bold"),
            bg=parent["bg"],
            fg=self.orange
        )

        title.pack(pady=(20, 10))

        return title


    def create_entry(self, parent, placeholder="", show=None):

        entry = tk.Entry(
            parent,
            font=("Arial", 13),
            width=32,
            bd=1,
            relief="solid",
            show=show
        )

        entry.pack(ipady=10, pady=7)

        return entry


    def create_button(self, parent, text, command, width=25):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            bg=self.orange,
            fg=self.white,
            activebackground=self.dark_orange,
            activeforeground=self.white,
            font=("Arial", 12, "bold"),
            relief="flat",
            cursor="hand2",
            bd=0
        )

        button.pack(ipady=9, pady=8)

        return button


    # =====================================================
    # WELCOME SCREEN
    # =====================================================

    def show_welcome(self):

        self.clear_screen()

        # Main background
        main = tk.Frame(self.root, bg=self.orange)
        main.pack(fill="both", expand=True)

        # Logo
        logo = tk.Label(
            main,
            text="DARAZ.PK",
            font=("Arial", 42, "bold"),
            bg=self.orange,
            fg=self.white
        )

        logo.pack(pady=(90, 5))


        subtitle = tk.Label(
            main,
            text="WELCOME TO DARAZ.PK",
            font=("Arial", 20, "bold"),
            bg=self.orange,
            fg=self.white
        )

        subtitle.pack(pady=10)


        description = tk.Label(
            main,
            text="Your account. Your shopping. Your world.",
            font=("Arial", 13),
            bg=self.orange,
            fg=self.white
        )

        description.pack(pady=10)


        # White card
        card = tk.Frame(
            main,
            bg=self.white,
            width=420,
            height=230
        )

        card.pack(pady=25)
        card.pack_propagate(False)


        question = tk.Label(
            card,
            text="Do you already have an account?",
            font=("Arial", 15, "bold"),
            bg=self.white,
            fg=self.dark
        )

        question.pack(pady=(25, 15))


        login_button = tk.Button(
            card,
            text="LOGIN",
            command=self.show_login,
            bg=self.orange,
            fg=self.white,
            font=("Arial", 12, "bold"),
            width=25,
            relief="flat",
            cursor="hand2"
        )

        login_button.pack(ipady=8, pady=5)


        signup_button = tk.Button(
            card,
            text="CREATE NEW ACCOUNT",
            command=self.show_signup,
            bg=self.white,
            fg=self.orange,
            font=("Arial", 12, "bold"),
            width=25,
            relief="solid",
            bd=1,
            cursor="hand2"
        )

        signup_button.pack(ipady=8, pady=5)


    # =====================================================
    # LOGIN SCREEN
    # =====================================================

    def show_login(self):

        self.clear_screen()

        background = tk.Frame(
            self.root,
            bg=self.light_gray
        )

        background.pack(fill="both", expand=True)


        # Left side
        left = tk.Frame(
            background,
            bg=self.orange,
            width=360
        )

        left.pack(side="left", fill="y")
        left.pack_propagate(False)


        tk.Label(
            left,
            text="DARAZ.PK",
            font=("Arial", 35, "bold"),
            bg=self.orange,
            fg=self.white
        ).pack(pady=(120, 10))


        tk.Label(
            left,
            text="WELCOME BACK!",
            font=("Arial", 20, "bold"),
            bg=self.orange,
            fg=self.white
        ).pack(pady=10)


        tk.Label(
            left,
            text="Login to continue shopping",
            font=("Arial", 12),
            bg=self.orange,
            fg=self.white
        ).pack()


        # Right side
        card = tk.Frame(
            background,
            bg=self.white,
            width=540
        )

        card.pack(side="right", fill="both", expand=True)


        tk.Label(
            card,
            text="Login",
            font=("Arial", 30, "bold"),
            bg=self.white,
            fg=self.dark
        ).pack(pady=(55, 25))


        # Gmail
        tk.Label(
            card,
            text="Gmail Account",
            font=("Arial", 11, "bold"),
            bg=self.white,
            fg=self.dark
        ).pack(anchor="w", padx=100)


        self.login_gmail = tk.Entry(
            card,
            font=("Arial", 13),
            width=32,
            relief="solid",
            bd=1
        )

        self.login_gmail.pack(ipady=9, pady=(5, 15))


        # Password
        tk.Label(
            card,
            text="Password",
            font=("Arial", 11, "bold"),
            bg=self.white,
            fg=self.dark
        ).pack(anchor="w", padx=100)


        password_frame = tk.Frame(
            card,
            bg=self.white
        )

        password_frame.pack()


        self.login_password = tk.Entry(
            password_frame,
            font=("Arial", 13),
            width=26,
            show="*",
            relief="solid",
            bd=1
        )

        self.login_password.pack(side="left", ipady=9)


        self.login_show = False

        tk.Button(
            password_frame,
            text="👁",
            command=self.toggle_login_password,
            font=("Arial", 11),
            bg=self.white,
            relief="solid",
            bd=1,
            cursor="hand2"
        ).pack(side="left", ipady=8)


        # Login button
        tk.Button(
            card,
            text="LOGIN",
            command=self.login,
            bg=self.orange,
            fg=self.white,
            font=("Arial", 12, "bold"),
            width=32,
            relief="flat",
            cursor="hand2"
        ).pack(ipady=10, pady=25)


        tk.Button(
            card,
            text="Don't have an account? Create one",
            command=self.show_signup,
            bg=self.white,
            fg=self.orange,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack()


        tk.Button(
            card,
            text="← Back",
            command=self.show_welcome,
            bg=self.white,
            fg=self.gray,
            relief="flat",
            cursor="hand2"
        ).pack(pady=15)


    # =====================================================
    # LOGIN PASSWORD SHOW / HIDE
    # =====================================================

    def toggle_login_password(self):

        self.login_show = not self.login_show

        if self.login_show:
            self.login_password.config(show="")
        else:
            self.login_password.config(show="*")


    # =====================================================
    # LOGIN FUNCTION
    # =====================================================

    def login(self):

        gmail = self.login_gmail.get().strip()
        password = self.login_password.get()


        if gmail == "" or password == "":
            messagebox.showwarning(
                "Missing Information",
                "Please enter your Gmail and password."
            )
            return


        if gmail in self.login_accounts_info:

            account = self.login_accounts_info[gmail]


            # New format
            if isinstance(account, dict):

                saved_password = account["password"]
                name = account["name"]

            # Old format
            else:

                saved_password = account
                name = "User"


            if password == saved_password:

                self.current_user = gmail
                self.current_name = name

                messagebox.showinfo(
                    "Login Successful",
                    f"WELCOME TO YOUR ACCOUNT IN DARAZ.PK\n\n"
                    f"Hello {name.upper()}!"
                )

                self.show_dashboard()

            else:

                messagebox.showerror(
                    "Login Failed",
                    "Incorrect password."
                )

        else:

            messagebox.showerror(
                "Login Failed",
                "This Gmail account does not exist.\n"
                "Please create an account first."
            )


    # =====================================================
    # SIGNUP SCREEN
    # =====================================================

    def show_signup(self):

        self.clear_screen()

        background = tk.Frame(
            self.root,
            bg=self.light_gray
        )

        background.pack(fill="both", expand=True)


        # Header
        header = tk.Frame(
            background,
            bg=self.orange,
            height=90
        )

        header.pack(fill="x")
        header.pack_propagate(False)


        tk.Label(
            header,
            text="DARAZ.PK",
            font=("Arial", 28, "bold"),
            bg=self.orange,
            fg=self.white
        ).pack(side="left", padx=40, pady=20)


        tk.Label(
            header,
            text="CREATE YOUR ACCOUNT",
            font=("Arial", 17, "bold"),
            bg=self.orange,
            fg=self.white
        ).pack(side="right", padx=40)


        # Main card
        card = tk.Frame(
            background,
            bg=self.white,
            width=600,
            height=460
        )

        card.pack(pady=25)
        card.pack_propagate(False)


        tk.Label(
            card,
            text="Create Account",
            font=("Arial", 26, "bold"),
            bg=self.white,
            fg=self.dark
        ).pack(pady=(15, 10))


        # Name
        tk.Label(
            card,
            text="Your Name",
            font=("Arial", 10, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=80)


        self.signup_name = self.create_entry(card)


        # Gmail
        tk.Label(
            card,
            text="Gmail Account",
            font=("Arial", 10, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=80)


        self.signup_gmail = self.create_entry(card)


        # Password
        tk.Label(
            card,
            text="Create Password",
            font=("Arial", 10, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=80)


        self.signup_password = self.create_entry(
            card,
            show="*"
        )


        # Confirm password
        tk.Label(
            card,
            text="Confirm Password",
            font=("Arial", 10, "bold"),
            bg=self.white
        ).pack(anchor="w", padx=80)


        self.signup_confirm = self.create_entry(
            card,
            show="*"
        )


        # Password requirements
        tk.Label(
            card,
            text="Password: 8+ characters, uppercase, lowercase, digit & special character",
            font=("Arial", 8),
            bg=self.white,
            fg=self.gray
        ).pack(pady=2)


        # Button
        tk.Button(
            card,
            text="CREATE ACCOUNT",
            command=self.create_account,
            bg=self.orange,
            fg=self.white,
            font=("Arial", 12, "bold"),
            width=30,
            relief="flat",
            cursor="hand2"
        ).pack(ipady=8, pady=8)


        tk.Button(
            card,
            text="Already have an account? Login",
            command=self.show_login,
            bg=self.white,
            fg=self.orange,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack()


    # =====================================================
    # PASSWORD VALIDATION
    # =====================================================

    def strong_password(self, password):

        special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"


        return (
            len(password) >= 8
            and any(ch.islower() for ch in password)
            and any(ch.isupper() for ch in password)
            and any(ch.isdigit() for ch in password)
            and any(ch in special_characters for ch in password)
        )


    # =====================================================
    # GMAIL VALIDATION
    # =====================================================

    def valid_gmail(self, gmail):

        pattern = r"^[A-Za-z0-9._%+-]+@gmail\.com$"

        return re.match(pattern, gmail) is not None


    # =====================================================
    # CREATE ACCOUNT
    # =====================================================

    def create_account(self):

        name = self.signup_name.get().strip()
        gmail = self.signup_gmail.get().strip()
        password = self.signup_password.get()
        confirm = self.signup_confirm.get()


        # Name check
        if name == "":

            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )

            return


        # Gmail check
        if not self.valid_gmail(gmail):

            messagebox.showerror(
                "Invalid Gmail",
                "ENTER A VALID GMAIL ACCOUNT\n\n"
                "Example: yourname@gmail.com"
            )

            return


        # Existing account
        if gmail in self.login_accounts_info:

            messagebox.showerror(
                "Account Exists",
                "This Gmail account is already registered.\n"
                "Please login instead."
            )

            return


        # Password strength
        if not self.strong_password(password):

            messagebox.showerror(
                "Weak Password",
                "⚠️ Simple password detected!\n\n"
                "Your password must contain:\n"
                "• At least 8 characters\n"
                "• Lowercase letter\n"
                "• Uppercase letter\n"
                "• Number\n"
                "• Special character"
            )

            return


        # Password confirmation
        if password != confirm:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match."
            )

            return


        # Save account
        self.login_accounts_info[gmail] = {
            "name": name,
            "password": password
        }


        self.save_accounts()


        messagebox.showinfo(
            "Account Created",
            f"MR/MS {name.upper()}\n\n"
            "YOUR ACCOUNT CREATED SUCCESSFULLY!\n\n"
            "Now login to your account."
        )


        self.show_login()


    # =====================================================
    # DASHBOARD
    # =====================================================

    def show_dashboard(self):

        self.clear_screen()


        # Top navigation
        navbar = tk.Frame(
            self.root,
            bg=self.orange,
            height=75
        )

        navbar.pack(fill="x")
        navbar.pack_propagate(False)


        tk.Label(
            navbar,
            text="DARAZ.PK",
            font=("Arial", 27, "bold"),
            bg=self.orange,
            fg=self.white
        ).pack(side="left", padx=30)


        tk.Button(
            navbar,
            text="LOGOUT",
            command=self.logout,
            bg=self.white,
            fg=self.orange,
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(side="right", padx=30, pady=20)


        # Main content
        main = tk.Frame(
            self.root,
            bg=self.light_gray
        )

        main.pack(fill="both", expand=True)


        tk.Label(
            main,
            text=f"Welcome, {self.current_name.upper()}!",
            font=("Arial", 30, "bold"),
            bg=self.light_gray,
            fg=self.dark
        ).pack(pady=(70, 10))


        tk.Label(
            main,
            text="WELCOME TO YOUR ACCOUNT IN DARAZ.PK",
            font=("Arial", 16),
            bg=self.light_gray,
            fg=self.orange
        ).pack(pady=10)


        # Fake shopping cards
        products = tk.Frame(
            main,
            bg=self.light_gray
        )

        products.pack(pady=35)


        self.product_card(
            products,
            "📱",
            "Electronics"
        ).grid(row=0, column=0, padx=15)


        self.product_card(
            products,
            "👕",
            "Fashion"
        ).grid(row=0, column=1, padx=15)


        self.product_card(
            products,
            "🏠",
            "Home & Living"
        ).grid(row=0, column=2, padx=15)


    # =====================================================
    # PRODUCT CARD
    # =====================================================

    def product_card(self, parent, icon, title):

        card = tk.Frame(
            parent,
            bg=self.white,
            width=190,
            height=150,
            relief="solid",
            bd=1
        )

        card.pack_propagate(False)


        tk.Label(
            card,
            text=icon,
            font=("Arial", 35),
            bg=self.white
        ).pack(pady=(15, 5))


        tk.Label(
            card,
            text=title,
            font=("Arial", 13, "bold"),
            bg=self.white,
            fg=self.dark
        ).pack()


        return card


    # =====================================================
    # LOGOUT
    # =====================================================

    def logout(self):

        answer = messagebox.askyesno(
            "Logout",
            "Are you sure you want to logout?"
        )


        if answer:

            self.current_user = None
            self.current_name = None

            self.show_welcome()


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = DarazApp(root)

    root.mainloop()