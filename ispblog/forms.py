from django.forms import ModelForm 
from .models import c_request , suport

class CreateBlogForm (ModelForm): 
    class Meta: 
        model = c_request
        fields = ('Date', 'package', 'phone', 'address',)
class create_applied_for_view  (ModelForm): 
    class Meta: 
        model = suport
        fields = ('question', 'active_package', 'phone', 'address',)