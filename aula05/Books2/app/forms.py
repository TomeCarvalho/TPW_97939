from django import forms


class BookSearchForm(forms.Form):
    book_title = forms.CharField(label='Title', max_length=100, required=False)
    author_name = forms.CharField(label='Author Name', max_length=70, required=False)
    publisher_name = forms.CharField(label='Publisher Name', max_length=70, required=False)


class AuthorInsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=70)
    email = forms.EmailField()
