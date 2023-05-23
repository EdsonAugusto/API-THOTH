from django.forms import TextInput

class MaskedTextInput(TextInput):
    def __init__(self, attrs=None):
        super(MaskedTextInput, self).__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += ' masked-input'
        else:
            self.attrs['class'] = 'masked-input'

    def render(self, name, value, attrs=None, renderer=None):
        if value:
            value = '●' * 8  # Replace with your desired masking character
        return super(MaskedTextInput, self).render(name, value, attrs, renderer)