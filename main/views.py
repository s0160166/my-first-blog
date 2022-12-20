from django.shortcuts import render, redirect
from .models import Info, Results
from .forms import InfoForm, ResultsForm
from datetime import datetime
from .calculate import Calculate

def index(request):
 #   tasks = Task.objects.all()             #получение всех объектов (список)
#    tasks = Task.objects.order_by('-id')
    info = Info.objects.order_by('-id')
    current_date = datetime.now().date()
    for inf in info:
        if inf.obrabotka != True:
            inf.age = current_date.year - inf.date_born.year
            alc = float(inf.alcogol)
            if float(inf.alcogol) >= 1:
                alc -= 1
            inf.micromorts = float(inf.micromorts) + float(inf.profession) + float(inf.hobby) + alc/3 + float(inf.cigarets) / 1.4
            inf.cigarets  = float(inf.cigarets)/1.4
            inf.alcogol = alc/3
            inf.obrabotka = True
            inf.save()
    return render(request, 'main/index.html', {'title': 'главная страница сайта', 'info': info})

def results(request):
 #   tasks = Task.objects.all()             #получение всех объектов (список)
#    tasks = Task.objects.order_by('-id')
    info = Info.objects.order_by('-id')
    current_date = datetime.now().date()

    for inf in info:
        people = Calculate(inf.age, inf.loan_balance, float(inf.micromorts)+float(inf.profession)
        +float(inf.hobby)+float(inf.alcogol)+float(inf.cigarets))

        res = Results(id = inf.id, sum=people.calc())
        res.save()

    results = Results.objects.order_by('-id')
    return render(request, 'main/results.html', {'title': 'главная страница сайта', 'results': results})


def create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        form.save()
        return redirect('home')
    form = InfoForm()
    context = {
        'form': form,
        'title': 'заполнение данных о клиенте',
    }
    return render(request, 'main/create.html', context)
