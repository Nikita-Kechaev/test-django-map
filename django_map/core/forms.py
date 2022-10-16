from django import forms


class FindForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label='Укажите город, который ищите :'
    )
    radius = forms.IntegerField(
        required=False,
        label='Укажите радиус для поиска окрестных городов(км) :'
    )
