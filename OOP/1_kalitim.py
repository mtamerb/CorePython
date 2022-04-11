# Türetilmş Sınıf

"""
Üst Sınıftan nitelik almak için kullanılır .

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

 Çoklu Kalıtım :

 class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

"""


class Employee:
    yukselme = 1.09

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.email = ad.lower() + "." + soyad.lower() + "@email.com"
        self.maas = maas

    def ad_soyad_gostermek(self):
        return "{} {}".format(self.ad, self.soyad)

    def zam(self):
        self.maas = int(self.maas * self.yukselme)


class Developer(Employee):
    yukselme = 2

    # Peki ya altSınıfımıza yeni argüman eklemek istersek ?

    def __init__(self, ad, soyad, maas, prog_dili):
        super().__init__(ad, soyad, maas)
        self.prog_dili = prog_dili

    def dev_kisisel_bilgi_vermek(self):
        return "{}  {}  {}  {}".format(self.ad, self.soyad, self.maas, self.prog_dili)


class Manager(Employee):
    def __init__(self, ad, soyad, maas, employees=None):
        super().__init__(ad, soyad, maas)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def emp_eklemek(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def emp_cikarmak(self, emp):
        self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--> " + emp.ad_soyad_gostermek())


# Employee Sınıfının özelliklerine Developer Sınıfından ulaştık ( miras aldık )

dev_1 = Developer("Burak", "Canseven", 6000, "Java - Python")
dev_2 = Employee("Ceyda", "Adıgüzel", 8000)
dev_3 = Employee("Selami", "Koç", 14000)

# print(help(Developer))


print(dev_3.email)
print(dev_1.ad_soyad_gostermek())

print(dev_1.maas)
dev_1.zam()
print(dev_1.maas)

print(dev_3.maas)
dev_3.zam()
print(dev_3.maas)

print(dev_1.dev_kisisel_bilgi_vermek())

manager_1 = Manager("Tamer", "Bilici", 60000, [dev_2])
print(manager_1.ad_soyad_gostermek())
manager_1.emp_eklemek(dev_1)
manager_1.emp_eklemek(dev_3)
manager_1.emp_cikarmak(dev_2)
manager_1.print_emp()

# instance kontrol : isinstance()

print(isinstance(manager_1, Developer))
print(isinstance(manager_1, Employee))
print(isinstance(dev_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
