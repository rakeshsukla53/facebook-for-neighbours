from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserModelForm, ThreadModelForm, MessageModelForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from register.models import Registration, History, Block, Hood
from django.utils import timezone
from django.views.generic import TemplateView


def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                q = Registration.objects.filter(uname=request.user)
                for i in q:
                    person, created = History.objects.get_or_create(uid=i)  # it will give you direct object
                    person.login_time = timezone.now()
                    person.save()

                return HttpResponseRedirect('/profile')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

    return render(request, "index.html")

def Logout(request):
    q = Registration.objects.filter(uname=request.user)
    for i in q:
        s = History.objects.filter(uid=i)  # here you get list of objects
        for j in s:  # here you can get actual object thats why you need to iterate
            j.logout_time = timezone.now()
            j.save()
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
    return render(request, "index/home.html", {})

def Blog(request):
    return render(request, "index/blog.html", {})

class RegistrationForm(FormView):
    template_name = 'index/register.html'
    form_class = UserModelForm
    success_url = '/home'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # validation can be done from here
        # you are getting cleaned data from form
        print form.cleaned_data
        user = form.cleaned_data['uname']
        password = form.cleaned_data['upassword']
        email = form.cleaned_data['uemail']
        # User.objects.create_user(username=user, email=email, password=password)
        form.save()  # I have to use signal here
        # you can easily just save the data
        # form.save()
        # this is how you will store and data here
        # name, address = form.cleaned_data['name'], form.cleaned_data['address']
        # Registration.objects.create(name=name, address=address)
        return super(RegistrationForm, self).form_valid(form)

class ThreadForm(FormView):
    template_name = 'thread.html'
    form_class = ThreadModelForm
    success_url = '/success'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ThreadForm, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ThreadForm, self).get_context_data(**kwargs)
        context['second_form'] = MessageModelForm
        return context

class ProfileTemplateView(TemplateView):

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['info'] = Registration.objects.get(uname=request.user)
        context['info_block'] = Block.objects.filter(hid=context['info'].uhid)
        context['value'] = 3
        context['info_friend'] = Registration.objects.filter(uhood=context['info'].uhood).exclude(uname=request.user)
        context['value_neigh'] = 6
        # objects get is for fetching only one row
        # objects filter is for fetching more than one row. You cannot fetch more than one row using get
        return self.render_to_response(context)

