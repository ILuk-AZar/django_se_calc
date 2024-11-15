from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Engine
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import CalculationHistory


@login_required
def calculate_engines(request):
    result = None
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        engines = Engine.objects.all()
        results = {}

        for engine in engines:
            results[engine.name] = -(-weight // engine.thrust)

        result = {'weight': weight, 'engines': results}

        # Сохраняем результат в историю пользователя
        CalculationHistory.objects.create(
            user=request.user,
            weight=weight,
            result=str(results)
        )

    return render(request, 'calculator/calculator.html', {'result': result})


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Создай шаблон home.html

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    history = CalculationHistory.objects.filter(user=request.user)
    return render(request, 'calculator/profile.html', {'history': history})
