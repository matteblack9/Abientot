from django.conrib.auth.models import User
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['word',]