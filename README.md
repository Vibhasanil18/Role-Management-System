# Role Management System

The **Role Management System** is a key module in the HR Management System designed to define and manage roles within an organization. It ensures a secure, organized workflow by providing role-based access to the system's data and functionality.

---

## Features

1. **Role Creation:**
   - Only Admin users can create roles like Admin, Manager, Team Leader, and Employee.

2. **Role Dashboard:**
   - View all roles with edit and delete options.
   - Button to create a new role.

3. **Update Role:**
   - Admin can update role details.
   - Automatically redirects to the dashboard after updating.

4. **Soft Delete Role:**
   - Only Admin can delete roles.
   - A warning message is displayed before deletion.
   - Implements a soft delete by marking the role as inactive in the database.

---

## Technologies Used

- **Backend:** Django
- **Frontend:** React (for dashboards) and HTML/CSS
- **Database:** MySQL (using XAMPP)

---

## Installation

Follow these steps to run the project on your local system:

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/RoleManagement.git
