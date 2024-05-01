  Coffee Shop Order Recording App (Python + Tkinter) Overview The Coffee Shop Order Recording App is a simple yet efficient Python application designed for coffee shop owners and staff to manage customer orders.
  Built using the Tkinter library for the graphical user interface (GUI) and MySQL Connector for database interaction, this app streamlines the order process, reduces manual effort, and maintains a record of sales.
  Features User-Friendly Interface: The app provides an intuitive interface where users can input drink details (type, size, and extras) easily. It displays a welcome message and prompts users to place their orders.
  Order Recording: Users can enter the type of drink (coffee or tea), select the size (small, medium, or large), and specify any extras (e.g., vanilla syrup). The app calculates the total price based on the selected options.
  Orders are stored in a MySQL database for future reference. Database Integration: The app connects to a local MySQL database (you can customize the connection details).
  Two tables are created: products (for product details) and sale (for order history). 
  Functionality: Add a new product (drink) to the database. Delete an existing product. 
  View all available products. Generate a bill for each order and store it in the database. 
  How to Use Installation: Ensure you have Python installed (preferably Python 3.x).
  Install the required modules: pip install mysql-connector pip install tkinter  Database Setup: Create a MySQL database named Shop.
  Run the provided SQL queries to create the necessary tables (products and sale). Run the App: Execute the Python script (coffeeshoporder.py).
  The GUI window will open, displaying the welcome message and input fields. 
  Enter the order details and click the “Place Order” button. Customization: Adjust prices, add more product options, or enhance the GUI as needed.
  Explore additional features like revenue calculation, order history display, etc.
  Project Files coffeeshoporder.py: Main Python script containing the app logic. 
  coffee_shop.sql: SQL file with table creation queries.
  Resources Python Shop Management System Project with Source Code GitHub: Billing-System-OR-Cafe-Restaurant-Managment-System-Using-Python-Tkinter-MySQL Feel free to customize and expand this app according to your coffee shop’s specific needs. 

  
#Amir_Akbari
#SXL
  
