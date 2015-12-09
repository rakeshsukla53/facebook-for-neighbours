from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Registration
# Create your views here.
from django.utils import timezone
from django.views.generic.detail import DetailView
# from .forms import RegistrationAddForm, RegistrationModelForm


# class RegistrationListView(ListView):
#     model = Registration
#     # if you can define your template as well here
#     # template_name = 'base.html'
#     # if you don't define the template then it automatically searches for template at `registration/registration_view` it will go into app name
#
#     def get_queryset(self, *args, **kwargs):
#         form = RegistrationAddForm()
#         context = super(RegistrationListView, self).get_queryset(**kwargs)
#         # you can give some filter command here whenever it is required
#         # context.filter(address__icontains = ""). You can also pass on some parameters
#         return context
#
#     def get_context_data(self, **kwargs):
#
#         '''
#         Here if you are just overiding the context data. Its the same context data if you use in views that pass on to template.
#         context - {u'paginator': None, u'registration_list': [<Registration: Rakesh>], u'object_list': [<Registration: Rakesh>], u'page_obj': None, 'now': datetime.datetime(2015, 11, 27, 1, 33, 34, 957354, tzinfo=<UTC>), u'is_paginated': False, u'view': <registration.views.RegistrationListView object at 0x7f7726590750>}
#         Object list contains the list of items from my model `Registration`
#         Registratin.objects.all() - this is your context list
#         '''
#
#         context = super(RegistrationListView, self).get_context_data(**kwargs)
#         # context['now'] = timezone.now()
#         # context['queryset'] = Registration.objects.all()
#         # there are lot of functions associated with ListView which you check out
#         # get_query is already defined in ListView class which you can directly use or you can define your own get_query function()
#         context['queryset'] = self.get_queryset()
#         # print context
#         return context
#
#
# class RegistrationDetailView(DetailView):
#     model = Registration
#
#     def get_context_data(self, **kwargs):
#         # print kwargs
#         obj = super(RegistrationDetailView, self).get_context_data(**kwargs)
#         obj['now'] = timezone.now()
#         return obj
#
