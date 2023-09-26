import tkinter as tk
from tkinter import messagebox

# Sample menu data (item_name: (item_price, item_quantity))
menu_items = {
    "Burger": (5.99, 10),
    "Pizza": (8.99, 15),
    "Pasta": (7.49, 12),
    "Salad": (4.99, 20),
}

class RestaurantManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Restaurant Management System")
        
        # Create a top frame for the menu display
        top_frame = tk.Frame(root)
        top_frame.pack()
        
        # Create a menu label
        menu_label = tk.Label(top_frame, text="Menu", font=("Helvetica", 16))
        menu_label.pack()
        
        # Create a menu frame for item buttons
        menu_frame = tk.Frame(top_frame)
        menu_frame.pack()
        
        # Create item buttons for each menu item
        for item in menu_items:
            item_button = tk.Button(menu_frame, text=f"{item} (${menu_items[item][0]:.2f})", command=lambda i=item: self.add_to_order(i))
            item_button.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Create a bottom frame for the order display and checkout
        bottom_frame = tk.Frame(root)
        bottom_frame.pack()
        
        # Create an order label
        order_label = tk.Label(bottom_frame, text="Your Order", font=("Helvetica", 16))
        order_label.pack()
        
        # Create an order listbox
        self.order_listbox = tk.Listbox(bottom_frame)
        self.order_listbox.pack()
        
        # Create a checkout button
        checkout_button = tk.Button(bottom_frame, text="Checkout", command=self.checkout)
        checkout_button.pack()
        
        # Initialize order data
        self.order = {}
    
    def add_to_order(self, item):
        if menu_items[item][1] == 0:
            messagebox.showwarning("Warning", f"{item} is out of stock.")
            return
        
        if item not in self.order:
            self.order[item] = 1
        else:
            self.order[item] += 1
        
        menu_items[item] = (menu_items[item][0], menu_items[item][1] - 1)
        
        # Update the order listbox
        self.update_order_listbox()
    
    def update_order_listbox(self):
        self.order_listbox.delete(0, tk.END)
        for item, quantity in self.order.items():
            self.order_listbox.insert(tk.END, f"{item} x{quantity}")
    
    def checkout(self):
        total_price = sum(menu_items[item][0] * quantity for item, quantity in self.order.items())
        messagebox.showinfo("Order Summary", f"Total Price: ${total_price:.2f}\nThank you for your order!")
        self.order = {}  # Reset the order
        self.update_order_listbox()
    
if _name_ == "_main_":
    root = tk.Tk()
    app = RestaurantManagementSystem(root)
    root.mainloop()
