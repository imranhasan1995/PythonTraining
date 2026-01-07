# getattr(), setattr(), hasattr()

info = ["name", "emp_id", "status"]
value = ["Imran", 40, "Present"]


class Emp:
    def __init__(self, name, emp_id, status):
        self.name = name
        self.emp_id = emp_id
        self.status = status


emp = Emp("Ansh", 30, "Present")
print("The information of Employee:")
for i in range(len(info)):
    print(getattr(emp, info[i]))
    setattr(emp, info[i], value[i])
    print("New Value:",getattr(emp, info[i]))
    print(f"property {info[i]} status:{hasattr(emp, info[i])}")

### print() function 
print("TutorialsPoint", "is", "located", "in", "India.", sep="-")
