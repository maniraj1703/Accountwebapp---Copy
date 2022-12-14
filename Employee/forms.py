
from django import forms
from .models import Employee
from django.contrib.auth.models import User
from Utils.utils import  isValidPhoneNumber, isNoneOrEmpty, isValidNumber, isValidText
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Eid', 'Name', 'Email', 'PhoneNo', 'Role', 'Salary', 'PF']


    def clean(self):
        """data from the form is fetched using super function"""
        super(EmployeeForm, self).clean()
         
        eid = self.cleaned_data.get('Eid')
        phNo = self.cleaned_data.get('PhoneNo')
        sal = self.cleaned_data.get('Salary')
        pf = self.cleaned_data.get('PF')
        name = self.cleaned_data.get('Name')
        role = self.cleaned_data.get('Role')

        eidMsg = isValidNumber(eid)
        phNoMsg = isValidPhoneNumber(phNo)
        salMsg = isValidNumber(sal)
        pfMsg = isValidNumber(pf)
        nameMsg = isValidText(name)
        roleMsg = isValidText(role)

        if isNoneOrEmpty(eidMsg) == False:
            self.errors['Eid'] = self.error_class([eidMsg])

        if isNoneOrEmpty(phNoMsg) == False:
            self.errors['PhoneNo'] = self.error_class([phNoMsg])

        if isNoneOrEmpty(salMsg) == False:
            self.errors['Salary'] = self.error_class([salMsg])

        if isNoneOrEmpty(pfMsg) == False:
            self.errors['PF'] = self.error_class([pfMsg])

        if isNoneOrEmpty(nameMsg) == False:
            self.errors['Name'] = self.error_class([nameMsg])

        if isNoneOrEmpty(roleMsg) == False:
            self.errors['Role'] = self.error_class([roleMsg])
        
        return self.cleaned_data
