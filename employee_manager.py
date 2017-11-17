import Employee
import pickle
ADD=1
EDIT=2
LOOK_UP=3
DELETE=4
QUIT=5
FILE_NAME='employees.txt'

def load_employees(file_name):
    try:
        employee_file=open(file_name,'rb')
        employee_dict=pickle.load(employee_file)
        employee_file.close()
    except IOError or EOFError:
        employee_dict={}
    return employee_dict

def add_employee(employees):
    print("\n---Add Employee---")
    employee_id=input('Enter Employee id: ')
    employee_name=input('Enter Employee Name: ')
    department=input('Enter department: ')
    job_title=input('Enter Job Title: ')
    employee=Employee.Employee(employee_id,employee_name,department,job_title)
    if employee_id not in employees:
        employees[employee_id]=employee
        print('Employee added in the dictionary')
    else:
        print('Employee Id '+employee_id+' is not present in the dictionary')

def edit_employee(employees):
    print("\n---Edit Employee---")
    employee_id=input('Enter Employee id: ')
    if employee_id not in employees:
        print('Employee Id '+employee_id+' is not present in the dictionary')
        return
    employee=employees[employee_id]
    employee_name=input('Enter Employee Name: ')
    department=input('Enter department: ')
    job_title=input('Enter Job Title: ')
    employee.set_employee_name(employee_name)
    employee.set_department(department)
    employee.set_job_title(job_title)
    employees[employee_id]=employee
    print('Employee updated in the dictionary')       
    
def lookup_employee(employees):
    print('\n---Lookup Employee---')
    employee_id=input('Enter Employee id: ')
    if employee_id not in employees:
        print('Employee Id '+employee_id+' is not present in the dictionary')
        return
    employee=employees[employee_id]
    print('\nEmployee Details:\n',employee)

def delete_employee(employees):
    print("\n---Delete Employee---")
    employee_id=input('Enter Employee id: ')
    if employee_id not in employees:
        print('Employee Id '+employee_id+' is not present in the dictionary')
    else:
        del employees[employee_id]
        print('Employee deleted')

def save_employees(employees,file_name):
    employee_file=open(file_name,'wb')
    pickle.dump(employees,employee_file)
    employee_file.close()
    
def main():
    employees=load_employees(FILE_NAME)
    again='y'
    while(again=='y'):
        print('-----------Employee Management System-------------\n1. Add Employee\n2. Edit Employee\n3. Search Employee \n4. Delete Employee \n5. Quit')
        choice=int(input('Enter your choice: '))
        if(choice==ADD):
            add_employee(employees)
        elif(choice==EDIT):
            edit_employee(employees)
        elif(choice==LOOK_UP):
            lookup_employee(employees)
        elif(choice==DELETE):
            delete_employee(employees)
        elif(choice==QUIT):
            again='n'
        else:
            print('Incorrect choice. Please try again')
        if(again=='y'):
            again=input("press 'y' to continue").lower()
    save_employees(employees,FILE_NAME)
    print('Thank you!')
main()