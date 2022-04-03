from django import forms
from .models import Signup


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"

    def clean(self):
        super(SignupForm, self).clean()

        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password')
        c_password = self.cleaned_data.get('confirm_password')
        mobno = self.cleaned_data.get('mobno')

        if len(first_name) < 3:
            self._errors['first_name'] = self.error_class(
                ['A min of 3 chars required for first name'])

        if len(last_name) < 3:
            self._errors['last_name'] = self.error_class(
                ['A min of 3 chars required for last name'])

        if len(mobno) != 10:
            self._errors['mobno'] = self.error_class(
                ['Enter Correct Mob No'])

        if password != c_password:
            self._errors['password'] = self.error_class(
                ['Password & Confirm Password Does Not Matches'])

            self._errors['c_password'] = self.error_class(
                ['Password & Confirm Password Does Not Matches'])

        return self.cleaned_data