from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserModelForm, ThreadModelForm, MessageModelForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from register.models import Registration, History, Block, Hood, Message, Thread, Neighbour
from register.models import AuthBlock
from django.utils import timezone
from django.views.generic import TemplateView, View, CreateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator

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
    success_url = '/feed'
    second_form = MessageModelForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreadForm, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ThreadForm, self).form_valid(form)

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        ttype = request.POST['ttype']
        mauthor = request.user
        mtext = request.POST['mtext']
        tdesc = request.POST['tdesc']
        t = Thread.objects.create(ttype=ttype, tauthor=Registration.objects.get(uname=request.user), tdesc=tdesc)
        Message.objects.create(tid=Thread.objects.get(tid=t.tid), mauthor=Registration.objects.get(uname=request.user), mtext=mtext)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

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
        names_to_exlude = [line.nuid2.uname for line in Neighbour.objects.filter(nuid1=Registration.objects.get(uname=request.user))]

        context['info_friend'] = Registration.objects.filter(uhood=context['info'].uhood).exclude(uname__in=names_to_exlude).exclude(uname=request.user)
        context['value_neigh'] = 6
        context['block_request'] = AuthBlock.objects.all()
        for auth in AuthBlock.objects.all():
            if auth.status:
                context['request_approve'] = auth.bid
                print auth.bid
        # objects get is for fetching only one row
        # objects filter is for fetching more than one row. You cannot fetch more than one row using get
        return self.render_to_response(context)

class FeedTemplateView(TemplateView):

    template_name = 'feed.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FeedTemplateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['Hood'] = Thread.objects.filter(ttype='HOOD')
        context['Block'] = Thread.objects.filter(ttype='BLOCK')
        context['value'] = 3
        context['value1'] = 7
        # objects get is for fetching only one row
        # objects filter is for fetching more than one row. You cannot fetch more than one row using get
        return self.render_to_response(context)

class ThreadMessageForm(TemplateView):

    template_name = 'message.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ThreadMessageForm, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = MessageModelForm
        context['messages'] = Message.objects.filter(tid=Thread.objects.filter(tid=kwargs['hood_id']))
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):

        tid = kwargs['hood_id']
        mtext = request.POST['mtext']
        Message.objects.create(tid=Thread.objects.get(tid=tid), mauthor=Registration.objects.get(uname=request.user), mtext=mtext)
        return HttpResponseRedirect('')

class FriendView(CreateView):

    def get(self, request, *args, **kwargs):
        print request.GET, kwargs, request.user
        Neighbour.objects.create(nuid1=Registration.objects.get(uname=request.user), nuid2=Registration.objects.get(uname=kwargs['friend_id']), hid=Hood.objects.get(hname=Registration.objects.get(uname=request.user).uhood))
        return HttpResponse('Friend is now Added')

class BlockView(CreateView):

    def get(self, request, *args, **kwargs):
        print request.GET, kwargs, request.user
        n = len(Block.objects.filter(hid=Hood.objects.get(hname=Registration.objects.get(uname=request.user).uhood)))
        AuthBlock.objects.create(uid=Registration.objects.get(uname=request.user), bid=Block.objects.get(bname=kwargs['block_id']), total_request_required=n, approval_received=0)
        return HttpResponse('Request is being sent for your block request')

class BlockRequest(CreateView):

    def get(self, request, *args, **kwargs):

        for line in AuthBlock.objects.all():
            line.approval_received += 1
            if line.approval_received == line.total_request_required:
                line.approved = True
                line.status = True
                line.save()
                break
            line.save()
            break
        return HttpResponse('Request is being approved now')


























