#define an employee class with attriutes role,department & salary.this class also have the showDetails() method .
#create an engineer class from employee & add age and name in it then show details

class employee:
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal
    
    def showDetails(self):
        print("role=",self.role,"\n""dep=",self.dep,"\n""sal=",self.sal)

class engineer(employee):
    def __init__(self, name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","IT","75000")

    
engg1=engineer("elon musk",40)
engg1.showDetails()
