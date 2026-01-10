import datetime

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def to_list(self):
        current_node = self.head
        lst = []
        while current_node:
            lst.append(current_node.data)
            current_node = current_node.next
        return lst

    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst.pop(len(lst) // 2)
        lower, greater = [], []
        for item in lst:
            (lower if item['username'] <= pivot['username'] else greater).append(item)
        return self.quick_sort(lower) + [pivot] + self.quick_sort(greater)

    def binary_search(self, lst, username):
        start, end = 0, len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            if lst[mid]['username'] == username:
                return lst[mid]
            elif lst[mid]['username'] < username:
                start = mid + 1
            else:
                end = mid - 1
        return None

    def find(self, username):
        lst = self.to_list()
        sorted_lst = self.quick_sort(lst)
        return self.binary_search(sorted_lst, username)
    
    def delChoice(self, student_data):
        currentNode = self.head
        previousNode = None

        while currentNode:
            if currentNode.data["username"] == student_data["username"]:
                if previousNode:
                    previousNode.next = currentNode.next
                else:
                    self.head = currentNode.next
                print(f"Student {student_data['username']} removed successfully.")
                return
            previousNode = currentNode
            currentNode = currentNode.next

        print(f"Student {student_data['username']} not found.")


    def display(self):
        current_node = self.head
        students = []
        while current_node:
            students.append(current_node.data)
            current_node = current_node.next
        return students

admins = LinkedList()
students = LinkedList()
rotc_schedule = []  
semester_start = None
semester_end = None
attendance_logs = {}

# Ensure at least one admin exists
if not admins.head:
    print("No admin account found. Please create an initial admin account.")
    initial_username = input("Enter Initial Admin Username: ").upper()
    initial_password = input("Enter Initial Admin Password: ")
    admins.append_end({"username": initial_username, "password": initial_password, "locked": False})

# Admin Login Function
def admin_login():
    attempts = 3
    while attempts > 0:
        username = input("Enter Admin Username: ").upper()
        password = input("Enter Password: ")
        admin = admins.find(username)
        if not admin:
            print("User Name does not exist.")
        elif admin['locked']:
            print("Account is locked.")
            return False
        elif admin['password'] == password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect Password. {attempts} attempts remaining.")
    print("Account locked due to too many failed attempts.")
    if admin:
        admin['locked'] = True
    return False

# Student Registration Function
def student_registration():
    print("\n--- Student Registration ---")
    while True:
        username = input("TUP User Name (Format: TUPM-XX-XXXX): ").upper()
        if students.find(username):
            print("TUP User Name already exists. Please use a different one.")
            continue
        if username.startswith("TUPM-") and len(username.split("-")[1]) == 2 and len(username.split("-")[2]) == 4:
            break
        else:
            print("Invalid format. Please follow TUPM-XX-XXXX.")

    name = input("Name (Last Name, First Name): ").upper()
    age = input("Age: ")
    address = input("Address: ").upper()
    while True:
        birth_date = input("Birth Date (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, birth_date.split("-"))
            if len(birth_date) == 10:
                break
        except ValueError:
            print("Invalid format. Please follow YYYY-MM-DD.")
    department = input("College Department: ").upper()
    year_section = input("Year and Section: ").upper()
    religion = input("Religion: ").upper()
    email = input("TUP Email: ")

    while True:
        password = input("Password: ")
        retype_password = input("Re-Type Password: ")
        if password == retype_password:
            break
        else:
            print("Passwords do not match. Please try again.")

    while True:
        nstp_component = input("NSTP Component (LTS, CWTS, ROTC): ").upper()
        if nstp_component in ["LTS", "CWTS", "ROTC"]:
            break
        else:
            print("Invalid component. Please choose LTS, CWTS, or ROTC.")

    student_data = {
    "name": name,
    "age": age,
    "address": address,
    "birth_date": birth_date,
    "department": department,
    "year_section": year_section,
    "religion": religion,
    "email": email,
    "username": username,
    "password": password,
    "nstp_component": nstp_component,
    "status": "Active"
    }
    
    if nstp_component == "ROTC":
        print("\n--- Cadet Profile ---")
        while True:
            cadet_type = input("Cadet Type (BASIC CADET or OFFICER): ").upper()
            if cadet_type in ["BASIC CADET", "OFFICER"]:
                break
            else:
                print("Invalid input. Please enter either 'BASIC CADET' or 'OFFICER'.")
        company = input("Company: ").upper()
        platoon = input("Platoon: ").upper()
        squad = input("Squad: ").upper()
        student_data.update({
            "cadet_type": cadet_type,
            "company": company,
            "platoon": platoon,
            "squad": squad
        })
        
    students.append_end(student_data)
    attendance_logs[username] = []
    action_history.push({"action": "register", "data": student_data})
    print("\nRegistration successful!")
    
# Student Login Function
def student_login():
    username = input("Enter TUP User Name: ").upper()
    password = input("Enter Password: ")
    student = students.find(username)
    if student and student['password'] == password:
        update_student_status()
        print("\n--- Student Profile ---")
        for key, value in student.items():
            if key != "password":
                print(f"{key}: {value}")
        print(f"Status: {student['status']}")
    else:
        print("Invalid login credentials.")


# Admin Functions to Set Semester Dates and Class Schedule
def set_semester_and_rotc_schedule():
    global semester_start, semester_end, rotc_schedule
    while True:
        try:
            semester_start = datetime.datetime.strptime(input("Enter Semester Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
            semester_end = datetime.datetime.strptime(input("Enter Semester End Date (YYYY-MM-DD): "), "%Y-%m-%d")
            if semester_start < semester_end:
                break
            else:
                print("Start date must be before end date. Please try again.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    rotc_schedule.clear()
    current_date = semester_start
    while current_date <= semester_end:
        if current_date.weekday() in [3]: 
            rotc_schedule.append(current_date)
        current_date += datetime.timedelta(days=1)

    print("Semester dates and class schedules have been set.")
    print("Class Schedule:", [date.strftime("%Y-%m-%d") for date in rotc_schedule])

    print("Semester dates and class schedules have been set.")

# Log Attendance Function
def log_attendance():
    username = input("Enter TUP User Name: ").upper()
    password = input("Enter Password: ")
    student = students.find(username)
    if student and student['password'] == password:
        today = datetime.datetime.now().date()
        print("Today's date:", today.strftime("%Y-%m-%d"))
         
        today_str = today.strftime("%Y-%m-%d")
        
        rotc_schedule_str = [date.strftime("%Y-%m-%d") for date in rotc_schedule]
        
        if today_str in rotc_schedule_str:
            if username not in attendance_logs:
                attendance_logs[username] = []
            attendance_logs[username].append(today)
            print("Attendance logged successfully.")
        else:
            print("Today is not a scheduled class day.")
            print("Scheduled class days:", rotc_schedule_str)
    else:
        print("Invalid username or password.")

# Check Attendance History Function
def check_attendance_history():
    username = input("Enter TUP User Name: ").upper()
    password = input("Enter Password: ")
    student = students.find(username)
    if student and student['password'] == password:
        print("\n--- Attendance History ---")
        for date in attendance_logs.get(username, []):
            print(date.strftime("%Y-%m-%d"))
    else:
        print("Invalid login credentials.")

# Admin View Attendance Logs Function
def view_attendance_logs():
    update_student_status()  
    for username, dates in attendance_logs.items():
        print(f"\n--- {username}'s Attendance ---")
        for date in dates:
            print(date.strftime("%Y-%m-%d"))
    
# Check and Update Student Status        
def update_student_status():
    today = datetime.date.today()
    for student in students.display():
        if student['nstp_component'] == "ROTC" or "CWTS" or "LTS":
            missed_days = 0
            username = student['username']
            attended_days = attendance_logs.get(username, []) 

            for current_date in rotc_schedule:
                current_date = current_date.date() 
                if current_date not in attended_days and current_date <= today:
                    missed_days += 1

            if missed_days >= 3:
                student['status'] = "Dropped"
            else:
                student['status'] = "Active"
            
def reset_at_end_of_semester():
    global students, attendance_logs, semester_end
    today = datetime.datetime.now().date()
    if semester_end is not None and today == semester_end.date():  
        print("\n--- Semester End Reached ---")
        
        students.head = None  
        
        attendance_logs = {}  
        print("All students have been removed, and attendance logs have been reset.")
        
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack

action_history = Stack() 

def undo_last_action():
    last_action = action_history.pop()
    if last_action:
        if last_action["action"] == "register":
            student_data = last_action["data"]
            
            students.delChoice(student_data)
            print(f"Undid registration for student {student_data['username']}")
        else:
            print("Unknown action to undo.")
    else:
        print("No actions to undo.")


# Main Program Loop
while True:
    reset_at_end_of_semester()
    update_student_status()
    
    print("\nNSTP APPLICATION AND ATTENDANCE TRACKER SYSTEM")
    user_type = input("Are you a Student or an Admin? (Enter 'Student' or 'Admin'): ").lower()

    if user_type == 'admin':
        if admin_login():
            while True:
                print("\n--- Admin Menu ---")
                print("1. View Students\n2. Search Student\n3. Create Admin User\n4. Reset Student List\n5. Set Semester Dates and NSTP Schedule\n6. View Attendance Logs\n7. Undo Recent Action \n8. Logout")
                choice = input("Choose an option: ")
                if choice == '1':
                    print("\n--- Student List ---")
                    student_list = students.display()
                    if not student_list:
                        print("No registered students at the moment.")
                    else:
                        for student in student_list:
                            for key, value in student.items():
                                if key != "password":
                                    print(f"{key}: {value}")
                            print("---")
                elif choice == '2':
                    search_username = input("Enter Student TUP User Name to Search: ").upper()
                    student = students.find(search_username)
                    if student:
                        for key, value in student.items():
                            if key != "password":
                                print(f"{key}: {value}")
                    else:
                        print("Student not found.")
                elif choice == '3':
                    new_admin_username = input("Enter New Admin Username: ").upper()
                    new_admin_password = input("Enter New Admin Password: ")
                    admins.append_end({"username": new_admin_username, "password": new_admin_password, "locked": False})
                    print("New admin user created successfully.")
                elif choice == '4':
                    students = LinkedList()
                    print("Student list reset successfully.")
                elif choice == '5':
                    set_semester_and_rotc_schedule()
                elif choice == '6':
                    view_attendance_logs()
                elif choice == '7':
                    undo_last_action()
                elif choice == '8':
                    print("Logging out...")
                    break
                else:
                    print("Invalid option. Please try again.")
    elif user_type == 'student':
        while True:
            print("\n--- Student Menu ---")
            print("1. NSTP Application \n2. Attendance Tracker\n3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                print("\nNSTP Application System")
                print("1. New Student \n2. Existing Student \n3. Exit")
                choice1 = input("Choose an option: ")
                if choice1 == '1':
                    student_registration()
                elif choice1 == '2':
                    student_login()
                elif choice1 == '3':
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            elif choice == '2':
                print("\nAttendance Tracker")
                print("1. Log Attendance \n2. Check Attendance History \n3. Exit")
                choice2 = input("Choose an option: ")
                if choice2 == '1':
                    log_attendance()
                elif choice2 == '2':
                    check_attendance_history()
                elif choice2 == '3':
                    break
                else:
                    print("Invalid input. Please enter 1, 2, or 3.")
            elif choice == '3':
                print("Exiting Student Menu...")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid user type. Please enter 'Student' or 'Admin'.")
