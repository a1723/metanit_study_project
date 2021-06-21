from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"myfield"}))
    #name = forms.CharField(label="Имя", initial="Sasha", help_text="Enter ur name")
    #age = forms.IntegerField(label="Возраст", initial=18)
    #comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
    email = forms.EmailField(label="Почта")
    #required_css_class = "field"
    #error_css_class = "error"
