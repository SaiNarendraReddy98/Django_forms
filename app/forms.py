from django import forms

g=[['Male','Male'],['Female','Female']]
c=[['python','python'],['Django','Django'],['sql','sql'],['java','java']]
class NameForm(forms.Form):
    Sname = forms.CharField()
    Sage = forms.IntegerField()
    Spassword = forms.CharField(widget=forms.PasswordInput)
    Sgender = forms.ChoiceField(choices=g)
    Courses = forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    Saddress = forms.CharField(widget=forms.Textarea(attrs={'cols':8,'rows':8}))

    