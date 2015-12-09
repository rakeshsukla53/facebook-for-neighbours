# from .models import Registration
# from django import forms
# from django.forms.extras.widgets import SelectDateWidget
#
#
# # we can directly pass the model to form using ModelForm
#
# class RegistrationModelForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields = ['name', 'address', 'image']
#
#     # clean field here
#     def clean_address(self):
#         # using these method you can clean your data as much as possible
#         address = self.cleaned_data['address']
#         if address < 50:
#             raise forms.ValidationError("address should be greater than 50")
#
#         return address
#
#
# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
# FAVORITE_COLORS_CHOICES = (
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# )
#
# # form widgets are absolutely amazing if you can have choice field so many other options
#
# class RegistrationAddForm(forms.Form):
#     name = forms.CharField(widget=forms.Textarea(attrs={"class": "my-custom-class", "placeholder": "name"}))
#     address = forms.IntegerField()
#     # whatever I am adding inside Passinput is custom form field holder
#     comment = forms.CharField(widget=forms.PasswordInput())
#     birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     favorite_colors = forms.MultipleChoiceField(required=False,
#         widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
#
#     def clean_address(self):
#         # using these method you can clean your data as much as possible
#         address = self.cleaned_data['address']
#         if address < 50:
#             raise forms.ValidationError("address should be greater than 50")
#
#         return address

