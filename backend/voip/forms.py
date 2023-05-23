from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashWidget
from .widgets import MaskedTextInput


from .models import Softswitch_VSC, Server_Gateway, Server_PABx, Server_Portability, Server_XenServer


class Softswitch_VSCAdminForm(forms.ModelForm):
    server_password = forms.CharField(
        label='Server Password',
        #widget=ReadOnlyPasswordHashWidget(),
        widget=MaskedTextInput(attrs={'readonly': 'readonly'}),
        help_text='To change the password, use the edit form for the Softswitch_VSC instance.'
    )

    class Meta:
        model = Softswitch_VSC
        fields = '__all__'


class Server_GatewayAdminForm(forms.ModelForm):
    server_password = forms.CharField(
        label='Server Password',
        #widget=ReadOnlyPasswordHashWidget(),
        widget=MaskedTextInput(attrs={'readonly': 'readonly'}),
        help_text='To change the password, use the edit form for the Server_Gateway instance.'
    )

    class Meta:
        model = Server_Gateway
        fields = '__all__'

class Server_PABxAdminForm(forms.ModelForm):
    server_password = forms.CharField(
        label='Server Password',
        #widget=ReadOnlyPasswordHashWidget(),
        widget=MaskedTextInput(attrs={'readonly': 'readonly'}),
        help_text='To change the password, use the edit form for the Server_Portability instance.'
    )

    class Meta:
        model = Server_PABx
        fields = '__all__'

class Server_PortabilityAdminForm(forms.ModelForm):
    server_password = forms.CharField(
        label='Server Password',
        #widget=ReadOnlyPasswordHashWidget(),
        widget=MaskedTextInput(attrs={'readonly': 'readonly'}),
        help_text='To change the password, use the edit form for the Server_Portability instance.'
    )

    class Meta:
        model = Server_Portability
        fields = '__all__'


class Server_XenServerAdminForm(forms.ModelForm):
    server_password = forms.CharField(
        label='Server Password',
        #widget=ReadOnlyPasswordHashWidget(),
        widget=MaskedTextInput(attrs={'readonly': 'readonly'}),
        help_text='To change the password, use the edit form for the Server_XenServer instance.'
    )

    class Meta:
        model = Server_XenServer
        fields = '__all__'