from django import forms
from django.contrib.auth.models import User
from .models import Order,Rewiews



class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone', 'email','adress','otdel', 'buying_type', 'comment'
        )



class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Логин'
        self.fields['password'].label = 'Пароль'
        
    def clean(self):
        username= self.cleaned_data['username']
        password= self.cleaned_data['password']
        if not User.objects.filter(username=username).exists() or User.objects.filter(email=username).exists():
            raise forms.ValidationError(f'Пользователь с логином или почтой  {username} не найден.')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data
    
    class Meta:
        model=User
        fields= ['username','password']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(required=True,max_length=30)
    text = forms.CharField(widget=forms.Textarea,max_length=500,help_text='Максимальное кол-во символов 500')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].label='Имя'
        self.fields['email'].label = 'Е-майл'
        self.fields['text'].label='Ваше сообщение'
        self.fields['text'].widget.attrs['rows'] = 4
        self.fields['text'].widget.attrs['columns'] = 15

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password=forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(required=True,help_text="+38-050-111-11-11")
    adress = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['email'].label='Электороная почта'
        self.fields['confirm_password'].label='Подтвердите пароль'
        self.fields['phone'].label = 'Номер телефона'
        self.fields['first_name'].label='Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['adress'].label='Адрес'
        

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(f'Данный e-mail уже зарегистрован')
        return self.cleaned_data['email']

    def clean_username(self):
        username= self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Имя {username} занято')
        return username
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password= self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    class Meta:
        model=User
        fields=['username','email','password','confirm_password','first_name','last_name','adress','phone']




class RewiewsForm(forms.ModelForm):
    # if not User.objects.get(user=request.user).exists():
    #         raise forms.ValidationError('Пользователь не залогинен')
    class Meta:
        model = Rewiews
        fields=('text',)
