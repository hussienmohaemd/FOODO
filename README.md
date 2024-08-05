# FOODO: Restaurant Management System

**FOODO** is a comprehensive restaurant management system designed to streamline user feedback and efficiently manage the menu, item catalog, and services within a restaurant.

## Features

- **Catalog Information**: Access detailed information about the restaurant's menu and services via the JSON endpoint at [http://localhost:5000/catalog/JSON](http://localhost:5000/catalog/JSON).
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on menu items and categories.
- **Authentication & Authorization**: Secure user authentication and authorization using Facebook and Google.

## Getting Started

### Prerequisites

Ensure you have the following software installed:

- **Vagrant**
- **VMware**
- **Flask**
- **Python**

### Installation

Follow these steps to set up and run the application:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/hussienmohaemd/FOODO
    cd FOODO
    ```

2. **Start Vagrant**

    ```bash
    cd vagrant
    vagrant up
    vagrant ssh
    ```

3. **Setup the Database**

    ```bash
    cd /vagrant/catalog
    python database_setup.py
    python lotsofmenus.py
    ```

4. **Run the Application**

    ```bash
    python project.py
    ```

5. **Access the Application**

    Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## Project Structure

- **static/**: Contains static files such as CSS, JavaScript, and images.
- **templates/**: HTML templates for rendering web pages.
- **README.md**: Project documentation.
- **app.py**: Main application script.
- **database_setup.py**: Script for setting up the database schema.
- **lotsofmenus.py**: Script for populating the database with sample data.
- **project.py**: Main script to run the project.

## Usage

### Endpoints

- **Catalog JSON**: Retrieve the entire catalog in JSON format.

    ```bash
    GET /catalog/JSON
    ```

- **Category Courses JSON**: Retrieve courses for a specific category in JSON format.

    ```bash
    GET /categories/<int:category_id>/courses/JSON
    ```

### User Authentication

- **Login**: Users can log in using their Facebook or Google accounts.
- **Register**: New users can register for an account.
- **Logout**: Users can log out from the application.

### CRUD Operations

- **Create**: Add new categories and courses.
- **Read**: View existing categories and courses.
- **Update**: Edit existing categories and courses.
- **Delete**: Remove categories and courses.

## Contact

For any queries or feedback, feel free to reach out:

- **Eng. Hussien**: [Facebook](https://facebook.com)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
