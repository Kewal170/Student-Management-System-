# Student Management System

A simple **Student Management System** built using Python's `Tkinter` for the GUI and `MySQL` (via `pymysql`) for database management. The application allows users to perform CRUD operations (Create, Read, Update, Delete) on student records and includes a search functionality.

## Features

- **Add New Student**: Allows users to input and add new student information (Roll No., Name, Email, Gender, Contact, Date of Birth, Address).
- **Update Student Details**: Users can modify existing student information.
- **Delete Student Record**: Users can remove student records from the database.
- **Search Student**: Provides a search feature based on Roll No., Name, or Contact.
- **Show All Students**: Displays all students' details in a table format.
- **Responsive UI**: Built with Tkinter, with a user-friendly interface and combo boxes for gender and search.

## Technologies Used

- **Python**: Tkinter for GUI, `pymysql` for MySQL database interaction.
- **MySQL**: Backend database for storing student information.
- **Tkinter**: Used for building the graphical user interface.

## Prerequisites

1. Install Python (3.x recommended).
2. Install MySQL or MySQL Server.
3. Install the required Python packages:

   ```bash
   pip install pymysql
   ```

4. Set up your MySQL database with the following table:

   ```sql
   CREATE DATABASE studentdb;

   USE studentdb;

   CREATE TABLE students (
     roll_no VARCHAR(10) PRIMARY KEY,
     name VARCHAR(100),
     email VARCHAR(100),
     gender VARCHAR(10),
     contact VARCHAR(15),
     dob VARCHAR(15),
     address TEXT
   );
   ```

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. Edit the database connection in the `add_students` method and other database operations to include your MySQL credentials.

3. Run the Python script:

   ```bash
   python student_management.py
   ```

4. The GUI will open, and you can start adding, updating, deleting, and searching student records.

## Contributing

If you'd like to contribute, feel free to fork the repository and submit a pull request.

