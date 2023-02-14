from django import forms
from django.forms import ModelForm
from .models import School
from django.urls import reverse_lazy
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class SchoolForm(forms.Form):

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.helper=FormHelper(self)
	# 	self.helper.form_action=reverse_lazy("index")
	# 	self.helper.form_method="GET"
	# 	self.helper.add_input(Submit('submit', 'Submit'))

	SUBJECT_CHOICES = (
		(1, "English"),
		(2, "Science"),
		(3, "Maths"),
	)

	title = forms.CharField(label="School Title", widget=forms.TextInput(attrs={"class":"title-field"}))
	subject = forms.ChoiceField(
		required=False,
		choices=SUBJECT_CHOICES
	)
	Year = forms.IntegerField()


class SchoolModelForm(ModelForm):
	class Meta:
		model = School
		#fields = '__all__'
		fields = ('name', 'address', 'summary',)