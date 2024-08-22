import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url+'/company/', params_to_add)
        return resp.json()

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]


    def create_company(self, name, description=""):
        company = {
		"name": name,
		"description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url+ '/company/', json=company, headers=my_headers)
        return resp.json()

    #def get_company(self, id):
        resp = requests.get(self.url+'/company/'+ str(id))
        return resp.json()

    #def edit(self, new_id, new_name, new_descr):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + '/company/' + str(new_id), headers = my_headers, json=company)
        return resp.json()


    #def delete(self,id):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.get(self.url + '/company/delete/' + str(id), headers=my_headers)
        return resp.json() 

    #def set_active_state(self, id, isActive):


    def add_new_employee(self, old_id, firstName, lastName, middleName, company_id, email, url, phone, birthdate, isActive):
        body = {
            "id": old_id,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "company_id": company_id,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee/', json=body,  headers=my_headers)
        return resp.json()

    def get_company_employee_list(self, id):
        my_param = {"company": id}
        resp = requests.get(self.url+'/employee/', json=my_param)
        return resp.json()


    def get_employee_by_id(self, id):
        my_param = {"employee": id}
        resp = requests.get(self.url + '/employee/', json=my_param)
        return resp.json()


    def edit_employee(self, new_employee_id, new_lastName, new_email, new_url, new_phone, isActive:True):
        body = {
            "lastName": new_lastName,
            "email": new_email,
            "url": new_url,
            "phone": new_phone,
            "isActive": isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/', + str(new_employee_id), json=body,  headers=my_headers)
        return resp.json()
