import requests


from CompanyApi import CompanyApi
api = CompanyApi("https://x-clients-be.onrender.com")


def test_get_companies():
	body = api.get_company_list()
	assert len(body) > 0


def test_get_active_companies():
	full_list = api.get_company_list()
	filtered_list = api.get_company_list(params_to_add={'active': 'true'})
	assert len(full_list) > len(filtered_list)


def test_add_new():
	body = api.get_company_list()
	len_before = len(body)
	name = "Autotest"
	descr = "Descr"
	result = api.create_company(name, descr)
	new_id = result['id']
	body = api.get_company_list()
	len_after = len(body)
	assert len_after - len_before == 1
	assert body[-1]["name"] == name
	assert body[-1]["description"] == descr
	assert body[-1]["id"] == new_id


def test_get_one_company():
	name = "VS Code"
	descr = "IDE"
	result = api.create_company(name, descr)
	new_id = result["id"]

	new_company = api.get_company(new_id)
	assert new_company["id"] == new_id
	assert new_company["name"] == name
	assert new_company["description"] == descr
	assert new_company["isActive"] == True


def test_edit():
	name = 'Company to be edited'
	descr = 'Edit me'
	result = api.create_company(name, descr)
	new_id = result['id']

	new_name = "UPDATED"
	new_descr = "_upd_"
	edited = api.edit(new_id, new_name, new_descr)
	assert edited["id"] == new_id
	assert edited["name"] == new_name
	assert edited["description"] == new_descr
	assert edited["isActive"] == True


def test_delete():
	name = 'Company to be deleted'
	descr = "Delete me"
	result = api.create_company(name, descr)
	new_id = result["id"]

	edited = api.delete(new_id)	

	assert edited["name"] == name
	assert edited["description"] == descr
	assert edited["isActive"] == True

	body = api.get_company_list()



def test_deactivate():
	name = 'Company to be deactivated'
	result = api.create_company(name)
	new_id = result["id"]
	
	body = api.set_active_state(new_id, False)
	assert body["isActive"] == False


def test_deactivate_and_activate_back():
	name = "Company to be deactivated"	
	result = api.create_company(name)
	new_id = result["id"]
	
	api.set_active_state(new_id, False)

	body = api.set_active_state(new_id, True)
	assert body["isActive"] == True

#Получить список сотрудников компании
def test_get_company_employee_list():

	#Добавить новую компанию
	name = "Компания для добавления сотрудника"
	descr = "IDE"
	result = api.create_company(name, descr)
	new_company_id = result["id"]

	#Добавить нового сотрудника
	old_id = 5
	firstName = "Елена"
	lastName = "Стах"
	middleName = "Владимировна"
	companyId = new_company_id
	email = "stahelenasr@gmail.com"
	url = " "
	phone = 89530958921
	birthdate = " "
	isActive: True
	result = api.add_new_employee(old_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate,True)
	new_employee_id = result.get("id")


#Получить список сотрудников компании
	id = new_company_id
	body = api.get_company_employee_list()
	assert len(body) > 0
	assert body[-1]["id"] == new_company_id