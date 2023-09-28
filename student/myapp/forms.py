from django import forms
from . models import Department,Course

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob =  forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    courses = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ChoiceField(choices=[('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials = forms.MultipleChoiceField(choices=[('notebook', 'Debit Note Book'), ('pen', 'Pen'), ('exam_papers', 'Exam Papers')], widget=forms.CheckboxSelectMultiple)
