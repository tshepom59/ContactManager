class Contact:
    def __init__(self,name,phone_number,email,website,bday,linkedin):
    	self.name = "name"
    	self.phone_number = phone_number
    	self.email = "email"
    	self.website = "website"
    	self.bday = bday
    	self.linkedin = "linkedin"

    	def name(self):
    		name = True

    	def phone_number(self):
    		phone_number = True

    	def email(self):
    		email = True

    	def website(self):
    		website = True

    	def bday(self):
    		bday = True

    	def linkedin(self):
    		linkedin = True

Mr_Morabane = Contact("Tshepo","none","tshepo.morabane@meltwater.org","none","none","tmorabane")

print(Mr_Morabane.email)