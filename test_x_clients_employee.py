import requests


from CompanyApi import CompanyApi
api = CompanyApi("https://x-clients-be.onrender.com")

#Получить список сотрудников компании
def test_get_company_employee_list():
	#Добавить новую компанию
	name = "Компания для добавления сотрудника"
	descr = "IDE"
	result = api.create_company(name, descr)
	new_company_id = result["id"]

	#Добавить нового сотрудника
	old_id = 0
	firstName ="Елена"
	lastName = "Стах"
	middleName ="Владимировна"
	company_id = new_company_id
	email = "stahelenasr@gmail.com"
	url = " "
	phone = "89530958920"
	birthdate = "1977-09-20"
	isActive: True
	result = api.add_new_employee(old_id, firstName, lastName, middleName, company_id, email, url, phone, birthdate, True)
	#new_employee_id = result.get ("id")
	list_after = api.get_employee_list(company_id)
	assert id_employee == list_after[0]['id']

#Получить список сотрудников компании
	id = new_company_id
	body = api.get_company_employee_list(id)
	assert len(body) > 0
	assert body.get("firstName") == firstName
	assert body["lastName"] == lastName
	assert body["company_id"] == new_company_id
test_x_clients1	assert body["isActive"] == True


#Получить информацию о сотруднике по id
def test_get_employee_by_id():
	# Добавить новую компанию
	name = "Компания для добавления сотрудника"
	descr = "IDE"
	result = api.create_company(name, descr)
	new_company_id = result["id"]

	# Добавить нового сотрудника
	old_id = 0
	firstName = "Елена"
	lastName = "Стах"
	middleName = "Владимировна"
	company_id = new_company_id
	email = "stahelenasr@gmail.com"
	url = " "
	phone = 89530958920
	birthdate = " "
	isActive: True
	result = api.add_new_employee(old_id, firstName, lastName, middleName, company_id, email, url, phone, birthdate,True)
	new_employee_id = result.get("id")
	assert result.get("id") == new_employee_id

	#Получить сотрудника по id
	id = new_employee_id
	body = api.get_employee_by_id(id)
	assert body["firstName"] == firstName
	assert body["lastName"] == lastName
	assert body["company_id"] == new_company_id
	assert body["isActive"] == True


#Отредактировать информацию о сотруднике
def test_edit_employee():
	# Добавить новую компанию
	name = "Компания для добавления сотрудника"
	descr = "IDE"
	result = api.create_company(name, descr)
	new_company_id = result["id"]

	# Добавить нового сотрудника
	old_id = 0
	firstName = "Елена"
	lastName = "Стах"
	middleName = "Владимировна"
	company_id = new_company_id
	email = "stahelenasr@gmail.com"
	url = " "
	phone = 89530958920
	birthdate = " "
	isActive: True
	result = api.add_new_employee(old_id, firstName, lastName, middleName, company_id, email, url, phone, birthdate,
								  True)
	new_employee_id = result.get("id")
	assert result.get("id") == new_employee_id

	# Отредактировать информацию о сотруднике
	new_lastName = "БК"
	new_email = "stah@mail.ru"
	new_url = "kkk"
	new_phone = 89530958925
	isActive: False
	result = api.edit_employee(new_lastName, new_email, new_url, new_phone, False)
	assert result["lastName"] == new_lastName
	assert result["url"] == new_url
	assert result["email"] == new_email
	assert result["phone"] == new_phone
	assert result["isActive"] == False
