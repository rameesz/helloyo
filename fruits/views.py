# fruits/views.py
from django.shortcuts import render ,redirect
from .models import FruitSet
from .forms import FruitSetForm

# View to add a fruit set
def add_fruit_set(request):
    if request.method == 'POST':
        form = FruitSetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_fruit_set')
    else:
        form = FruitSetForm()
    return render(request, 'fruits/add_fruit_set.html', {'form': form})

# View to search for a fruit set
def search_fruit_set(request):
    if request.method == 'POST':
        fruit1 = request.POST.get('fruit1')
        fruit2 = request.POST.get('fruit2')
        fruit3 = request.POST.get('fruit3')
        fruit4 = request.POST.get('fruit4')
        fruit5 = request.POST.get('fruit5')


        results = FruitSet.objects.filter(fruit1=fruit1, fruit2=fruit2, fruit3=fruit3, fruit4=fruit4, fruit5=fruit5)
        
        return render(request, 'fruits/search_results.html', {'results': results})
    
    return render(request, 'fruits/search_fruit_set.html')


def dashboard(request):
    # Fetch the latest 5 fruit sets
    recent_fruit_sets = FruitSet.objects.order_by('-id')[:5]
    
    return render(request, 'fruits/dashboard.html', {'recent_fruit_sets': recent_fruit_sets})