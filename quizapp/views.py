from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from .models import Mymodel
from django.urls import reverse_lazy

# Create your views here.

class Quiz_Welcome_Page(ListView):
    model=Mymodel
    template_name = 'index.html'

class Quiz_Page1(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question1.html'

class Quiz_Page2(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question2.html'

class Quiz_Page3(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question3.html'

class Quiz_Page4(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question4.html'

class Quiz_Page5(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question5.html'

class Quiz_Page6(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question6.html'

class Quiz_Page7(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question7.html'

class Quiz_Page8(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question8.html'

class Quiz_Page9(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question9.html'

class Quiz_Page10(CreateView):
    model = Mymodel
    fields = '__all__'
    template_name = 'question10.html'

class Quiz_Result(ListView):
    model = Mymodel
    fields = '__all__'
    template_name = 'result.html'
