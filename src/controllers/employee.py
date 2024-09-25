
class Employee:
    def __init__(self, f_name, l_name, age, dpi, nit,  address, phone , email, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.dpi = dpi
        self.nit = nit
        self.address = address
        self.phone = phone
        self.email = email
        self.gender = gender

        self.photo = None

        #other attributes
        self.birth_date = None
        self.s_marital_status = None

        #emergency contact
        self.sos_name_1 = None
        self.sos_contact_1 = None
        self.sos_name_2 = None
        self.sos_contact_2 = None

        #nationality
        self.nationality = None
        self.passport = None
    
        #employment
        self.occupation = None
        self.department = None
        
        self.initial_salary = None
        self.salary = None
        self.bonus = None
        self.other_bonus = None

        self.start_date = None
        self.end_date = None
        
        self.igss = None
        self.benefits = None

        


