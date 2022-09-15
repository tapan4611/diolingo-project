from django import forms  
from employee.models import Employee,Catagory  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"

class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = "__all__"

