import tkinter as tk
from tkinter import PhotoImage, messagebox

# Class to manage the cart (Dictionary used for cart storage)
class CartManager:
    def __init__(self):
        self.cart = {}  # Dictionary to store items and quantity

    def add_to_cart(self, item):
        self.cart[item] = self.cart.get(item, 0) + 1

    def remove_all(self):
        self.cart.clear()

    def get_cart_items(self):
        return [(item, quantity) for item, quantity in self.cart.items()]  # Returns list of tuples

# Class to store user information (Tuple used for structured data)
class UserInfo:
    def __init__(self, name, phone, email, family_members):
        self.details = (name, phone, email, family_members)  # Using a tuple to store user details

    def get_info(self):
        return self.details

# Main Application
class FoodPantryApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1300")
        self.root.title("CCS Food Pantry Request System")
        self.root.configure(bg="dark blue") 

        # Cart Manager Instance
        self.cart_manager = CartManager()

        # Main Label
        tk.Label(root, text="CCS Food Pantry Request System", bg="lime green", fg="white", font=('Comic Sans MS', 35)).pack(padx=250, pady=250)

        # Main Button
        tk.Button(root, text="Open Selection", bg="lime green", fg="white", font=('Comic Sans MS', 25), command=self.open_new_window).pack()

    def open_new_window(self):
        self.root.destroy()
        top = tk.Tk()
        top.geometry("1500x1300")
        top.title("Food Selection")

        # Background image
        self.bg_image = PhotoImage(file=r"veggies2.png")
        tk.Label(top, image=self.bg_image).place(relheight=1, relwidth=1)

        # Item Selection Label
        tk.Label(top, text="Select Your Items", bg="lime green", fg="white", font=('Comic Sans MS', 45)).pack(padx=155, pady=155)

        # Categories List (Using List)
        categories = [
            "Grains & Bread", 
            "Canned Goods", 
            "Protein and Dairy", 
            "Fruits and Veggies", 
            "Snacks & Beverages", 
            "Household Essentials"
        ]

        buttonframe = tk.LabelFrame(top)
        for i, category in enumerate(categories):
            btn = tk.Button(buttonframe, text=f"{category}", font=('Arial', 25), 
                            command=lambda cat=category: self.add_to_cart(cat))
            btn.grid(row=i//3, column=i%3, sticky=tk.W+tk.E)
            btn.config(bg="lime green", fg="white")

        buttonframe.pack(padx=50, pady=50, expand=True)

        # Cart Display
        self.cart_listbox = tk.Listbox(top, height=6, font=('Arial', 15))
        self.cart_listbox.pack(pady=10)

        # Buttons
        tk.Button(top, text="Empty Cart", bg="lime green", fg="white", font=('Comic Sans MS', 20), 
                  command=self.clear_cart).pack()
        tk.Button(top, text="Checkout", bg="lime green", fg="white", font=('Comic Sans MS', 25), 
                  command=lambda: self.checkout(top)).pack()

    def add_to_cart(self, item):
        self.cart_manager.add_to_cart(item)
        self.update_cart_display()

    def update_cart_display(self):
        self.cart_listbox.delete(0, tk.END)
        for item, quantity in self.cart_manager.get_cart_items():
            self.cart_listbox.insert(tk.END, f"{item} x {quantity}")

    def clear_cart(self):
        self.cart_manager.remove_all()
        self.update_cart_display()

    def checkout(self, top):
        if not self.cart_manager.get_cart_items():
            messagebox.showwarning("Empty Cart", "Your cart is empty!")
            return

        top.destroy()
        checkout_window = tk.Tk()
        checkout_window.geometry("1500x1300")
        checkout_window.title("Checkout")
        checkout_window.configure(bg="dark blue")

        # Input Fields
        tk.Label(checkout_window, text="Name:", bg="lime green", fg="white", font=('Comic Sans MS', 30)).pack()
        name_entry = tk.Entry(checkout_window, width=30)
        name_entry.pack(pady=20)

        tk.Label(checkout_window, text="Phone Number:", bg="lime green", fg="white", font=('Comic Sans MS', 30)).pack()
        phone_entry = tk.Entry(checkout_window, width=30)
        phone_entry.pack(pady=20)

        tk.Label(checkout_window, text="Email:", bg="lime green", fg="white", font=('Comic Sans MS', 30)).pack()
        email_entry = tk.Entry(checkout_window, width=30)
        email_entry.pack(pady=20)

        tk.Label(checkout_window, text="Number of Family Members:", bg="lime green", fg="white", font=('Comic Sans MS', 30)).pack()
        family_entry = tk.Entry(checkout_window, width=30)
        family_entry.pack(pady=20)

        def place_order():
            if not all((name_entry.get(), phone_entry.get(), email_entry.get(), family_entry.get())):
                messagebox.showerror("Incomplete Information", "Please fill out all fields.")
                return

            user = UserInfo(name_entry.get(), phone_entry.get(), email_entry.get(), family_entry.get())

            messagebox.showinfo("Order Placed", f"Order successfully placed!\n\nUser Details:\n"
                                                f"Name: {user.details[0]}\n"
                                                f"Phone: {user.details[1]}\n"
                                                f"Email: {user.details[2]}\n"
                                                f"Family Members: {user.details[3]}")
            checkout_window.destroy()

        tk.Button(checkout_window, text="Place Order", bg="lime green", fg="white", font=('Comic Sans MS', 20), 
                  command=place_order).pack()

        tk.Button(checkout_window, text="Exit", bg="white", fg="red", font=('Comic Sans MS', 20), 
                  command=checkout_window.destroy).pack(side=tk.RIGHT, padx=10, pady=15, anchor=tk.SE)

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodPantryApp(root)
    root.mainloop()
