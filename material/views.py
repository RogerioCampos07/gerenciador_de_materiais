from django.shortcuts import get_object_or_404, render
from material.models import Material


def index(request):
    lista = Material.objects.all()
    context = {'lista':lista}
    return render(request,'material/index.html',context)





