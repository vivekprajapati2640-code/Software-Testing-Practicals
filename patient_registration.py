name = input("Enter patient name: ")
age = input("Enter age: ")
contact = input("Enter contact number: ")

if name.strip() and age.strip() and contact.strip():
    print("Patient Registered Successfully")
else:
    print("Registration Failed")