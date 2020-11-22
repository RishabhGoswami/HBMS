from django.shortcuts import render,redirect,get_object_or_404
from .models import Facility,Category,Room,Booking,contact
from .forms import ContactForm
from django.contrib.auth.models import User
from django.views.generic import CreateView,ListView,DeleteView
# Create your views here.
def index(request):
    papa=Category.objects.all()
    m=Facility.objects.all().order_by('-id')[:4]
    d={'m':m,'papa':papa}
    return render(request,'hotel/index.html',d)
def categorydetail(request,pk):
    ss=Room.objects.get(id=pk)
    p=Category.objects.all()
    context={'ss':ss,'p':p}
    return render(request,'hotel/x.html',context)
def gallery(request):
    pic=Room.objects.all()
    p=Category.objects.all()
    context={'pic':pic,'p':p}
    return render(request,'hotel/gallery.html',context)
def about(request):
    papa=Category.objects.all()
    return render(request,'hotel/about.html',{'papa':papa})
def facility(request):
    pm=Facility.objects.all()
    p=Category.objects.all()
    context={'pm':pm,'p':p}
    return render(request,'hotel/facility.html',context)
class BookCreateView(CreateView):
    model=Booking
    fields=['name','emailid','Idetitity','BookingDate','ArrivalDate','DepartureDate','gender','address','roomid']
    def form_valid(self,form):
        form.instance.userid=self.request.user
        return super().form_valid(form)
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(BookCreateView, self).get_form(form_class)
        form.fields['DepartureDate'].widget.attrs ={'placeholder': 'dd-mm-yyyy','class':'BookCreateView'}
        form.fields['BookingDate'].widget.attrs ={'placeholder': 'dd-mm-yyyy','class':'BookCreateView'}
        form.fields['ArrivalDate'].widget.attrs ={'placeholder': 'dd-mm-yyyy','class':'BookCreateView'}
        return form
class UserListView(ListView):
    model=Booking
    template_name='hotel/seeBooking.html'
    context_object_name='pp'
    def get_queryset(self):
        user=get_object_or_404(User,username=self.request.user)
        return Booking.objects.filter(userid=user)
class BookDeleteView(DeleteView):
    model=Booking
    success_url='/'
class ContactCreateView(CreateView):
    model=contact
    fields=['email','phonenumber','query']
    def form_valid(self,form):
        form.instance.name=self.request.user
        return super().form_valid(form)
class ContactListView(ListView):
    model=contact
    template_name='hotel/seequeries.html'
    context_object_name='ppp'
    def get_queryset(self):
        user=get_object_or_404(User,username=self.request.user)
        return contact.objects.filter(name=user)
def complete(request):
    return render(request,'hotel/complete.html')