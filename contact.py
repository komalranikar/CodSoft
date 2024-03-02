import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("450x400")
        self.root.configure(bg='#E0FFFF')  # Light Blue background

        # Contact list
        self.contacts = []

        # Labels and Entry widgets
        tk.Label(root, text="Name:", font=('Times New Roman', 16, 'bold'), bg='#E0FFFF').grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(root, font=('Times New Roman', 16))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone:", font=('Times New Roman', 16, 'bold'), bg='#E0FFFF').grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.phone_entry = tk.Entry(root, font=('Times New Roman', 16))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email:", font=('Times New Roman', 16, 'bold'), bg='#E0FFFF').grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.email_entry = tk.Entry(root, font=('Times New Roman', 16))
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Address:", font=('Times New Roman', 16, 'bold'), bg='#E0FFFF').grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.address_entry = tk.Entry(root, font=('Times New Roman', 16))
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        tk.Button(root, text="Add Contact", font=('Times New Roman', 16, 'bold'), command=self.add_contact, bg='#4169E1', fg='white').grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(root, text="View Contacts", font=('Times New Roman', 16, 'bold'), command=self.view_contacts, bg='#4169E1', fg='white').grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(root, text="Search Contact", font=('Times New Roman', 16, 'bold'), command=self.search_contact, bg='#4169E1', fg='white').grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        tk.Button(root, text="Delete Contact", font=('Times New Roman', 16, 'bold'), command=self.delete_contact, bg='#4169E1', fg='white').grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name is required.")

    def view_contacts(self):
        if self.contacts:
            contact_info = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_info)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        name_to_search = self.name_entry.get()

        if name_to_search:
            found_contacts = [contact for contact in self.contacts if contact['Name'] == name_to_search]
            if found_contacts:
                contact_info = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_info)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Enter name to search.")

    def delete_contact(self):
        name_to_delete = self.name_entry.get()

        if name_to_delete:
            for contact in self.contacts:
                if contact['Name'] == name_to_delete:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("Error", "Contact not found.")
        else:
            messagebox.showerror("Error", "Enter name to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
