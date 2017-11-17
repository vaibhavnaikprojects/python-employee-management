class Employee:
	def __init__(self,employee_id,employee_name,department,job_title):
		self.__employee_id=employee_id
		self.__employee_name=employee_name
		self.__department=department
		self.__job_title=job_title
	
	def set_employee_id(self,employee_id):
		self.__employee_id=employee_id
	
	def get_employee_id(self):
		return self.__employee_id
	
	def set_employee_name(self,employee_name):
		self.__employee_name=employee_name
	
	def get_employee_name(self):
		return self.__employee_name
	
	def set_department(self,department):
		self.__department=department
	
	def get_department(self):
		return self.__department
	
	def set_job_title(self,job_title):
		self.__job_title=job_title
		
	def get_job_title(self):
		return self.__job_title
	
	def __str__(self):
		return '\nEmployee Id: '+self.__employee_id+ '\nEmployee Name: '+self.__employee_name+'\nDepartment: '+self.__department+'\nJob Title: '+self.__job_title