# Hospital Management System

## Overview
The Hospital Management System is a Python-based application designed to manage hospital operations effectively. It allows for the addition, reading, searching, and deletion of patient and doctor records, providing a simple yet robust solution for hospital administration.

## Features

### Patient Management
- **Add Patient Record**: Enter and store new patient details.
- **Read All Patient Records**: Display all stored patient records.
- **Search Patient by ID**: Find a specific patient using their unique ID.
- **Delete Patient by ID**: Remove a patient's record from the system.

### Doctor Management
- **Add Doctor Record**: Enter and store new doctor details.
- **Read All Doctor Records**: Display all stored doctor records.
- **Search Doctor by ID**: Find a specific doctor using their unique ID.
- **Delete Doctor by ID**: Remove a doctor's record from the system.

## Installation

Clone the repository:
```bash
git clone https://github.com/MuhammadHarisTariq/Hospital-Management-System.git
```
Navigate to the project directory::
```bash
  cd hospital-management-system
```
Run the application:
```bash
  python hospital_management_system.py
```
## Usage
Upon running the application, you will be presented with the main menu, allowing you to choose between managing patient records or doctor records. Follow the on-screen prompts to perform the desired operation
### Main Menu
- **Patient Department**
- **Doctor Department**
- **Exit**
### Patient Management Menu
- **Add Patient Record**
- **Read All Patient Records**
- **Search Patient by ID**
- **Delete Patient by ID**
- **Go Back to Main Menu**

### Doctor Management Menu
- **Add Doctor Record**
- **Read All Doctor Records**
- **Search Doctor by ID**
- **Delete Doctor by ID**
- **Go Back to Main Menu**

## Code Structure

- **main()**: The entry point of the application, displays the main menu.
- **homeP()**: Manages patient-related operations.
- **homeD()**: Manages doctor-related operations.
- **writeP()**: Adds a new patient record.
- **readP()**: Displays all patient records.
- **searchByIdP()**: Searches for a patient by ID.
- **deleteP()**: Deletes a patient record by ID.
- **writeD()**: Adds a new doctor record.
- **readD()**: Displays all doctor records.
- **searchByIdD()**: Searches for a doctor by ID.
- **deleteD()**: Deletes a doctor record by ID.

## Conclusion

The Hospital Management System is a comprehensive and user-friendly solution for managing hospital records. By facilitating the efficient handling of patient and doctor data, it streamlines administrative tasks and enhances operational efficiency. We hope this system proves valuable to your hospital's management needs. Your feedback and suggestions are always welcome to further improve this project.
