

# **📝 To-Do List (Shell + Python + Linux)**  
![GitHub Repo Stars](https://img.shields.io/github/stars/Kunal-sonawanee/todo-list-shell-python?style=social)  
![GitHub Forks](https://img.shields.io/github/forks/Kunal-sonawanee/todo-list-shell-python?style=social)  
![GitHub Issues](https://img.shields.io/github/issues/Kunal-sonawanee/todo-list-shell-python)  
 

🚀 **A simple yet powerful To-Do List application** built using **Python and Shell scripting** for Linux users. This project provides **GUI support, database integration, and voice command functionality** to enhance task management.  

---

## **✨ Features**  Here’s your **updated `README.md`** with improvements, including instructions to **change the MySQL username and password**, along with **clarifications on database setup**:  

---

```md
# **📝 To-Do List (Shell + Python + Linux)**  
![GitHub Repo Stars](https://img.shields.io/github/stars/Kunal-sonawanee/todo-list-shell-python?style=social)  
![GitHub Forks](https://img.shields.io/github/forks/Kunal-sonawanee/todo-list-shell-python?style=social)  
![GitHub Issues](https://img.shields.io/github/issues/Kunal-sonawanee/todo-list-shell-python)  

🚀 **A simple yet powerful To-Do List application** built using **Python and Shell scripting** for Linux users. This project provides **GUI support, database integration, and voice command functionality** to enhance task management.  

---

## **✨ Features**  
✅ **Graphical User Interface (GUI)** – Easy-to-use task management 🖥️  
✅ **Database Support** – Saves tasks persistently using **MySQL** 🗃️  
✅ **Speech Recognition** – Add tasks using voice commands 🎙️  
✅ **Task Management** – Add, delete, update, and mark tasks as done ✅  
✅ **Command-Line Support** – Manage tasks directly from the terminal 💻  
✅ **Shell Scripting** – Automates task handling for efficiency 🐧  

---

## **📂 Project Structure**  
```
/todo-list-shell-python
│── todo_app.py          # Main Python script (GUI + database + voice)
│── README.md            # Project documentation
│── requirements.txt     # Required dependencies
```

---

## **📌 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Kunal-sonawanee/todo-list-shell-python.git
cd todo-list-shell-python
```

### **2️⃣ Install Dependencies**  
Ensure Python and required libraries are installed:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Configure the MySQL Database**  
#### **🔹 Update MySQL Credentials in `todo_app.py`**
Before running the app, you need to configure the **MySQL username and password** in `todo_app.py`:
```python
db = mysql.connector.connect(
    host="localhost", 
    user="your_mysql_username",  # Change this
    password="your_mysql_password",  # Change this
    database="todo_db"
)
```
Replace **`your_mysql_username`** and **`your_mysql_password`** with your actual MySQL credentials.

#### **🔹 Create the Database Manually**
If the database doesn't exist, create it manually in MySQL:
```sql
CREATE DATABASE todo_db;
USE todo_db;
```
The application will automatically create the required `tasks` table.

---

### **4️⃣ Run the Application**  
```bash
python todo_app.py
```

---

## **💡 Usage Guide**  
| Action | Description |  
|---------|------------|  
| `Add Task` | Add a new task manually or via speech |  
| `Delete Task` | Remove a specific task |  
| `Mark as Done` | Mark a task as completed |  
| `View Tasks` | Display all pending/completed tasks |  
| `Voice Command` | Say `"Add Grocery Shopping"` to add tasks |  

---

## **📈 Future Enhancements**  
🚀 **Task Prioritization (High, Medium, Low)**  
🚀 **Dark Mode & Custom Themes**  
🚀 **Cloud Sync & Multi-Device Support**  
🚀 **AI-Based Task Suggestions**  
🚀 **Email & SMS Reminders**  

---

## **🛠️ Requirements**  
To install required dependencies, run:  
```bash
pip install -r requirements.txt
```
### Dependencies in `requirements.txt`:  
- `PyQt6`  
- `mysql-connector-python`  
- `SpeechRecognition`  
- `PyAudio`  
- `plyer`  

---

## **🤝 Contributing**  
1. Fork the repository 📌  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Make changes & commit:  
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push the changes:  
   ```bash
   git push origin feature-branch
   ```
5. Open a **Pull Request** 🚀  

---

## **📜 License**  
This project is licensed under the **MIT License** – feel free to use and modify it.  

---

## **📞 Contact & Support**  
💬 Have questions or suggestions? Reach out via:  
📧 **Email:** sonawanekunal289@gmail.com  
🔗 **GitHub Issues:** [Report a bug or request a feature](https://github.com/Kunal-sonawanee/todo-list-shell-python/issues)  

---

## **🌟 Show Some Love**  
If you like this project, consider **starring ⭐ the repo** and sharing it with others!  

🔥 _Happy Coding!_ 🚀  
```

---

### **🔹 What's Updated?**  
✅ **MySQL Setup Instructions** (Guide users to change username & password)  
✅ **Database Creation Instructions** (Manually create `todo_db` if needed)  
✅ **Clearer Steps for Running the App**  

---

### **📌 Now, push the updated README to GitHub**
Run these commands:
```bash
git add README.md
git commit -m "Updated README with MySQL setup instructions"
git push origin main
```

Now your **GitHub repo is fully documented!** 🚀🔥 Let me know if you need further tweaks. 😊
✅ **Graphical User Interface (GUI)** – Easy-to-use task management 🖥️  
✅ **Database Support** – Saves tasks persistently using **SQLite** 🗃️  
✅ **Speech Recognition** – Add tasks using voice commands 🎙️  
✅ **Task Management** – Add, delete, update, and mark tasks as done ✅  
✅ **Command-Line Support** – Manage tasks directly from the terminal 💻  
✅ **Shell Scripting** – Automates task handling for efficiency 🐧  

---

## **📂 Project Structure**  
```
/todo-list-shell-python
│── todo_app.py          # Main Python script (GUI + database + voice)
│── README.md            # Project documentation
│── requirements.txt     # Required dependencies
```

---

## **📌 Installation & Setup**  
### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/todo-list-shell-python.git
cd todo-list-shell-python
```

### **2️⃣ Install Dependencies**  
Ensure Python and required libraries are installed:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Application**  
```bash
python todo_app.py
```


## **💡 Usage Guide**  
| Action | Description |  
|---------|------------|  
| `Add Task` | Add a new task manually or via speech |  
| `Delete Task` | Remove a specific task |  
| `Mark as Done` | Mark a task as completed |  
| `View Tasks` | Display all pending/completed tasks |  
| `Voice Command` | Say `"Add Grocery Shopping"` to add tasks |  


## **📈 Future Enhancements**  
🚀 **Task Prioritization (High, Medium, Low)**  
🚀 **Dark Mode & Custom Themes**  
🚀 **Cloud Sync & Multi-Device Support**  
🚀 **AI-Based Task Suggestions**  
🚀 **Email & SMS Reminders**  


## **🤝 Contributing**  
1. Fork the repository 📌  
2. Create a new branch: `git checkout -b feature-branch`  
3. Make changes & commit: `git commit -m "Added a new feature"`  
4. Push the changes: `git push origin feature-branch`  
5. Open a **Pull Request** 🚀  



## **📜 License**  
This project is licensed under the **MIT License** – feel free to use and modify it.  



## **📞 Contact & Support**  
💬 Have questions or suggestions? Reach out via:  
📧 **Email:** sonawanekunal289@gmail.com  
🔗 **GitHub Issues:** [Report a bug or request a feature](https://github.com/Kunal-sonawanee/todo-list-shell-python/issues)  



## **🌟 Show Some Love**  
If you like this project, consider **starring ⭐ the repo** and sharing it with others!  

🔥 _Happy Coding!_ 🚀  
