import tkinter as tk
from tkinter import messagebox

# Function to add a new patient record
def writeP():
    def save_record():
        id = id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        mobile = mobile_entry.get()
        department = dept_entry.get()
        salary = salary_entry.get()

        with open('PatientPy.txt', 'a') as file:
            file.write(f"{id}\t\t{name}\t\t{age}\t\t{mobile}\t\t{department}\t\t{salary}\n")

        messagebox.showinfo('Info', 'Patient record added successfully.')
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add New Patient Record")

    tk.Label(add_window, text="Patient ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Age:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Patient Mobile:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Department:").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Salary:").grid(row=5, column=0, padx=10, pady=5)

    id_entry = tk.Entry(add_window)
    name_entry = tk.Entry(add_window)
    age_entry = tk.Entry(add_window)
    mobile_entry = tk.Entry(add_window)
    dept_entry = tk.Entry(add_window)
    salary_entry = tk.Entry(add_window)

    id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    age_entry.grid(row=2, column=1, padx=10, pady=5)
    mobile_entry.grid(row=3, column=1, padx=10, pady=5)
    dept_entry.grid(row=4, column=1, padx=10, pady=5)
    salary_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save_record).grid(row=6, columnspan=2, pady=10)
    
#Function to Update Patient Records
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
                    dept_entry.insert(0, fields[4])
                    salary_entry.insert(0, fields[5].strip())
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Patient not found!')

    def update():
        id = id_entry.get()
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_mobile = mobile_entry.get()
        new_dept = dept_entry.get()
        new_salary = salary_entry.get()

        with open('PatientPy.txt', 'r') as file:
            lines = file.readlines()

        with open('PatientPy.txt', 'w') as file:
            updated = False
            for line in lines:
                fields = line.split('\t\t')
                if fields[0] == id:
                    file.write(f"{id}\t\t{new_name}\t\t{new_age}\t\t{new_mobile}\t\t{new_dept}\t\t{new_salary}\n")
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

    tk.Label(update_window, text="Department:").grid(row=5, column=0, padx=10, pady=5)
    dept_entry = tk.Entry(update_window)
    dept_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Salary:").grid(row=6, column=0, padx=10, pady=5)
    salary_entry = tk.Entry(update_window)
    salary_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Update", command=update).grid(row=7, columnspan=2, pady=10)

#Function to update doctors records
def updateD():
    def search():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[0] == id:
                    name_entry.insert(0, fields[1])
                    specialization_entry.insert(0, fields[2].strip())
                    found = True
                    break
            if not found:
                messagebox.showerror('Error', 'Doctor not found!')

    def update():
        id = id_entry.get()
        new_name = name_entry.get()
        new_specialization = specialization_entry.get()

        with open('DoctorPy.txt', 'r') as file:
            lines = file.readlines()

        with open('DoctorPy.txt', 'w') as file:
            updated = False
            for line in lines:
                fields = line.split('\t\t')
                if fields[0] == id:
                    file.write(f"{id}\t\t{new_name}\t\t{new_specialization}\n")
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

    tk.Button(update_window, text="Update", command=update).grid(row=4, columnspan=2, pady=10)
    
# Function to read and display all patient records
def readP():
    display_window = tk.Toplevel(root)
    display_window.title("All Patient Records")

    with open('PatientPy.txt', 'r') as file:
        data = file.read()

    tk.Text(display_window, wrap='word', width=80, height=20).pack(padx=10, pady=10)
    text_box = tk.Text(display_window, wrap='word', width=80, height=20)
    text_box.insert('1.0', data)
    text_box.pack(padx=10, pady=10)

# Function to search for a patient by ID
def searchByIdP():
    def search():
        id = id_entry.get()
        with open('PatientPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[0] == id:
                    result_var.set(f"ID\t\tName\t\tAge\t\tMobile\t\tDepartment\t\tSalary\n{'-' * 95}\n{line}")
                    found = True
                    break
            if not found:
                result_var.set("Patient not found!")

    search_window = tk.Toplevel(root)
    search_window.title("Search Patient by ID")

    tk.Label(search_window, text="Enter Patient ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(search_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)

    result_var = tk.StringVar()
    tk.Label(search_window, textvariable=result_var).grid(row=2, columnspan=2, padx=10, pady=10)

# Function to delete a patient record by ID
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

# Function to display the Patient Management menu
def homeP():
    menu_window = tk.Toplevel(root)
    menu_window.title("Patient Management Menu")

    tk.Button(menu_window, text="Add Patient Record", command=writeP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Read All Patient Records", command=readP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Search Patient by ID", command=searchByIdP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Delete Patient by ID", command=deleteP, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Update Patient Record", command=updateP, width=20).pack(padx=10, pady=10)

# Function to add a new doctor record
def writeD():
    def save_record():
        id = id_entry.get()
        name = name_entry.get()
        specialization = specialization_entry.get()

        with open('DoctorPy.txt', 'a') as file:
            file.write(f"{id}\t\t{name}\t\t{specialization}\n")

        messagebox.showinfo('Info', 'Doctor record added successfully.')
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add New Doctor Record")

    tk.Label(add_window, text="Doctor ID:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_window, text="Doctor Name:").grid(row=1, column=0, padx=10,    pady=5)
    tk.Label(add_window, text="Specialization:").grid(row=2, column=0, padx=10, pady=5)

    id_entry = tk.Entry(add_window)
    name_entry = tk.Entry(add_window)
    specialization_entry = tk.Entry(add_window)

    id_entry.grid(row=0, column=1, padx=10, pady=5)
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    specialization_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(add_window, text="Save", command=save_record).grid(row=3, columnspan=2, pady=10)

# Function to read and display all doctor records
def readD():
    display_window = tk.Toplevel(root)
    display_window.title("All Doctor Records")

    with open('DoctorPy.txt', 'r') as file:
        data = file.read()

    tk.Text(display_window, wrap='word', width=80, height=20).pack(padx=10, pady=10)
    text_box = tk.Text(display_window, wrap='word', width=80, height=20)
    text_box.insert('1.0', data)
    text_box.pack(padx=10, pady=10)

# Function to search for a doctor by ID
def searchByIdD():
    def search():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            found = False
            for line in file:
                fields = line.split('\t\t')
                if fields[0] == id:
                    result_var.set(f"ID\t\tName\t\tSpecialization\n{'-' * 50}\n{line}")
                    found = True
                    break
            if not found:
                result_var.set("Doctor not found!")

    search_window = tk.Toplevel(root)
    search_window.title("Search Doctor by ID")

    tk.Label(search_window, text="Enter Doctor ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(search_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(search_window, text="Search", command=search).grid(row=1, columnspan=2, pady=10)

    result_var = tk.StringVar()
    tk.Label(search_window, textvariable=result_var).grid(row=2, columnspan=2, padx=10, pady=10)

# Function to delete a doctor record by ID
def deleteD():
    def delete():
        id = id_entry.get()
        with open('DoctorPy.txt', 'r') as file:
            lines = file.readlines()

        with open('DoctorPy.txt', 'w') as file:
            found = False
            for line in lines:
                fields = line.split('\t\t')
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

# Function to display the Doctor Management menu
def homeD():
    menu_window = tk.Toplevel(root)
    menu_window.title("Doctor Management Menu")

    tk.Button(menu_window, text="Add Doctor Record", command=writeD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Read All Doctor Records", command=readD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Search Doctor by ID", command=searchByIdD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Delete Doctor by ID", command=deleteD, width=20).pack(padx=10, pady=10)
    tk.Button(menu_window, text="Update Doctor Record", command=updateD, width=20).pack(padx=10, pady=10)
# Function to display the main menu
def main():
    global root
    root = tk.Tk()
    root.title("Hospital Management System")

    tk.Button(root, text="Patient Department", command=homeP, width=20).pack(padx=10, pady=10)
    tk.Button(root, text="Doctor Department", command=homeD, width=20).pack(padx=10, pady=10)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(padx=10, pady=10)

    root.mainloop()

# Run the main function
main()

