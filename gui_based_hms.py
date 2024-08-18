import tkinter as tk
from tkinter import messagebox

def writeP():
    def save_record():
        id = id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        mobile = mobile_entry.get()
        disease = disease_entry.get()

        with open('PatientPy.txt', 'a') as file:
            file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{disease}\n")

        messagebox.showinfo('Info', 'Patient record added successfully.')
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add New Patient Record")

    tk.Label(add_window, text="Patient ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Age:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Mobile:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Disease:").grid(row=4, column=0, padx=10, pady=5)

    id_entry = tk.Entry(add_window)
    name_entry = tk.Entry(add_window)
    age_entry = tk.Entry(add_window)
    mobile_entry = tk.Entry(add_window)
    disease_entry = tk.Entry(add_window)

    id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    age_entry.grid(row=2, column=1, padx=10, pady=5)
    mobile_entry.grid(row=3, column=1, padx=10, pady=5)
    disease_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save_record).grid(row=5, columnspan=2, pady=10)

def updateP():
    def search():
        id = id_entry.get()
        with open('PatientPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[0] == id:
                    name_entry.insert(0, fields[1])
                    age_entry.insert(0, fields[2])
                    mobile_entry.insert(0, fields[3])
                    disease_entry.insert(0, fields[4].strip())
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Patient not found!')

    def update():
        id = id_entry.get()
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_mobile = mobile_entry.get()
        new_disease = disease_entry.get()

        with open('PatientPy.txt', 'r') as file:
            lines = file.readlines()

        with open('PatientPy.txt', 'w') as file:
            updated = False
            for line in lines:
                fields = line.split('\t\t')
                if fields[0] == id:
                    file.write(f"{id}\t\t{new_name}\t\t{new_age}\t\t{new_mobile}\t\t{new_disease}\n")
                    updated = True
                else:
                    file.write(line)
            if updated:
                messagebox.showinfo('Info', 'Patient record updated successfully.')
                update_window.destroy()
            else:
                messagebox.showerror('Error', 'Patient not found!')

    update_window = tk.Toplevel(root)
    update_window.title("Update Patient Record")

    tk.Label(update_window, text="Patient ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(update_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)

    tk.Label(update_window, text="Patient Name:").grid(row=2, column=0, padx=10, pady=5)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Patient Age:").grid(row=3, column=0, padx=10, pady=5)
    age_entry = tk.Entry(update_window)
    age_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Patient Mobile:").grid(row=4, column=0, padx=10, pady=5)
    mobile_entry = tk.Entry(update_window)
    mobile_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Disease:").grid(row=5, column=0, padx=10, pady=5)
    disease_entry = tk.Entry(update_window)
    disease_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Update", command=update).grid(row=6, columnspan=2, pady=10)

def readP():
    display_window = tk.Toplevel(root)
    display_window.title("All Patient Records")

    formatted_data = ""
    with open('PatientPy.txt', 'r') as file:
        for line in file:
            fields = line.strip().split('\t\t')
            formatted_data += (f"ID: {fields[0]}\n"
                               f"Name: {fields[1]}\n"
                               f"Age: {fields[2]}\n"
                               f"Mobile: {fields[3]}\n"
                               f"Disease: {fields[4]}\n\n")

    text_box = tk.Text(display_window, wrap='word', width=80, height=20)
    text_box.insert('1.0', formatted_data)
    text_box.pack(padx=10, pady=10)
    
def searchByIdP():
    def search():
        id = id_entry.get()
        with open('PatientPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.strip().split('\t\t')
                if fields[0] == id:
                    result_text = (f"ID: {fields[0]}\n"
                                   f"Name: {fields[1]}\n"
                                   f"Age: {fields[2]}\n"
                                   f"Mobile: {fields[3]}\n"
                                   f"Disease: {fields[4]}")
                    
                    result_window = tk.Toplevel(search_window)
                    result_window.title(f"Patient ID: {id}")
                    
                    text_box = tk.Text(result_window, wrap='word', width=60, height=10)
                    text_box.insert('1.0', result_text)
                    text_box.pack(padx=10, pady=10)
                    
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Patient not found!')

    search_window = tk.Toplevel(root)
    search_window.title("Search Patient by ID")

    tk.Label(search_window, text="Enter Patient ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(search_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)

def deleteP():
    def delete():
        id = id_entry.get()
        with open('PatientPy.txt', 'r') as file:
            lines = file.readlines()

        with open('PatientPy.txt', 'w') as file:
            found = False
            for line in lines:
                fields = line.split('\t\t')
                if fields[0] == id:
                    found = True
                else:
                    file.write(line)

            if found:
                messagebox.showinfo('Info', 'Patient record deleted successfully.')
                delete_window.destroy()
            else:
                messagebox.showerror('Error', 'Patient not found!')

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Patient Record")

    tk.Label(delete_window, text="Enter Patient ID to delete:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(delete_window, text="Delete", command=delete).grid(row=1, columnspan=2, pady=10)

def homeP():
    menu_window = tk.Toplevel(root)
    menu_window.title("Patient Management Menu")
    menu_window.geometry("400x400")

    tk.Button(menu_window, text="Add Patient Record", command=writeP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Read All Patient Records", command=readP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Search Patient by ID", command=searchByIdP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Delete Patient by ID", command=deleteP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Update Patient Record", command=updateP, width=20).pack(padx=10, pady=10)

def writeD():
    def save_record():
        id = id_entry.get()
        name = name_entry.get()
        specialization = specialization_entry.get()
        age = age_entry.get()
        mobile = mobile_entry.get()

        with open('DoctorPy.txt', 'a') as file:
            file.write(f"{id}\t{name}\t{specialization}\t{age}\t{mobile}\n")

        messagebox.showinfo('Info', 'Doctor record added successfully.')
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add New Doctor Record")

    tk.Label(add_window, text="Doctor ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Doctor Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Specialization:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Age:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Mobile:").grid(row=4, column=0, padx=10, pady=5)

    id_entry = tk.Entry(add_window)
    name_entry = tk.Entry(add_window)
    specialization_entry = tk.Entry(add_window)
    age_entry = tk.Entry(add_window)
    mobile_entry = tk.Entry(add_window)

    id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    specialization_entry.grid(row=2, column=1, padx=10, pady=5)
    age_entry.grid(row=3, column=1, padx=10, pady=5)
    mobile_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save_record).grid(row=5, columnspan=2, pady=10)

def readD():
    display_window = tk.Toplevel(root)
    display_window.title("All Doctor Records")

    formatted_data = ""
    with open('DoctorPy.txt', 'r') as file:
        for line in file:
            fields = line.strip().split('\t')
            formatted_data += (f"ID: {fields[0]}\n"
                               f"Name: {fields[1]}\n"
                               f"Specialization: {fields[2]}\n"
                               f"Age: {fields[3]}\n"
                               f"Mobile: {fields[4]}\n\n")

    text_box = tk.Text(display_window, wrap='word', width=80, height=20)
    text_box.insert('1.0', formatted_data)
    text_box.pack(padx=10, pady=10)

def searchByIdD():
    def search():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.strip().split('\t')
                if fields[0] == id:
                    result_text = (f"ID: {fields[0]}\n"
                                   f"Name: {fields[1]}\n"
                                   f"Specialization: {fields[2]}\n"
                                   f"Age: {fields[3]}\n"
                                   f"Mobile: {fields[4]}")
                    
                    result_window = tk.Toplevel(search_window)
                    result_window.title(f"Doctor ID: {id}")
                    
                    text_box = tk.Text(result_window, wrap='word', width=60, height=10)
                    text_box.insert('1.0', result_text)
                    text_box.pack(padx=10, pady=10)
                    
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Doctor not found!')

    search_window = tk.Toplevel(root)
    search_window.title("Search Doctor by ID")

    tk.Label(search_window, text="Enter Doctor ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(search_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)
   
def deleteD():
    def delete():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            lines = file.readlines()

        with open('DoctorPy.txt', 'w') as file:
            found = False
            for line in lines:
                fields = line.split('\t')
                if fields[0] == id:
                    found = True
                else:
                    file.write(line)

            if found:
                messagebox.showinfo('Info', 'Doctor record deleted successfully.')
                delete_window.destroy()
            else:
                messagebox.showerror('Error', 'Doctor not found!')

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Doctor Record")

    tk.Label(delete_window, text="Enter Doctor ID to delete:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(delete_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(delete_window, text="Delete", command=delete).grid(row=1, columnspan=2, pady=10)

def updateD():
    def search():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t')
                if fields[0] == id:
                    name_entry.insert(0, fields[1])
                    specialization_entry.insert(0, fields[2])
                    age_entry.insert(0, fields[3])
                    mobile_entry.insert(0, fields[4].strip())
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Doctor not found!')

    def update():
        id = id_entry.get()
        new_name = name_entry.get()
        new_specialization = specialization_entry.get()
        new_age = age_entry.get()
        new_mobile = mobile_entry.get()

        with open('DoctorPy.txt', 'r') as file:
            lines = file.readlines()

        with open('DoctorPy.txt', 'w') as file:
            updated = False
            for line in lines:
                fields = line.split('\t')
                if fields[0] == id:
                    file.write(f"{id}\t{new_name}\t{new_specialization}\t{new_age}\t{new_mobile}\n")
                    updated = True
                else:
                    file.write(line)

            if updated:
                messagebox.showinfo('Info', 'Doctor record updated successfully.')
                update_window.destroy()
            else:
                messagebox.showerror('Error', 'Doctor not found!')

    update_window = tk.Toplevel(root)
    update_window.title("Update Doctor Record")

    tk.Label(update_window, text="Doctor ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(update_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)

    tk.Label(update_window, text="Doctor Name:").grid(row=2, column=0, padx=10, pady=5)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Specialization:").grid(row=3, column=0, padx=10, pady=5)
    specialization_entry = tk.Entry(update_window)
    specialization_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Age:").grid(row=4, column=0, padx=10, pady=5)
    age_entry = tk.Entry(update_window)
    age_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Mobile:").grid(row=5, column=0, padx=10, pady=5)
    mobile_entry = tk.Entry(update_window)
    mobile_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Update", command=update).grid(row=6, columnspan=2, pady=10)

def homeD():
    menu_window = tk.Toplevel(root)
    menu_window.title("Doctor Management Menu")
    menu_window.geometry("400x400")

    tk.Button(menu_window, text="Add Doctor Record", command=writeD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Read All Doctor Records", command=readD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Search Doctor by ID", command=searchByIdD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Delete Doctor by ID", command=deleteD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Update Doctor Record", command=updateD, width=20).pack(padx=10, pady=10)

def main():
    global root
    root = tk.Tk()
    root.title("Hospital Management System")
    root.geometry('400x400')

    tk.Button(root, text="Patient Department", command=homeP, width=20).pack(padx=10, pady=10)
    tk.Button(root, text="Doctor Department", command=homeD, width=20).pack(padx=10, pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(padx=10, pady=10)

    root.mainloop()

main()



