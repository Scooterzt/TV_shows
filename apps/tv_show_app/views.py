from django.shortcuts import render, redirect
from .models import Shows

def shows(request):
    context = {
        "shows" : Shows.objects.all()
    }
    return render(request, "tv_show_app/shows.html", context)

def new(request):
    return render(request, "tv_show_app/new.html")

def display_show(request, show_id):
    context={
        "show": Shows.objects.get(id=show_id),
    }
    return render (request, "tv_show_app/display_show.html", context)

def add_show(request):
    new_show = Shows.objects.create(
        title=request.POST["show_title"],
        network=request.POST["network"],
        release_date=request.POST["release_date"],
        decription=request.POST["decription"],
        )
    return redirect("/shows")

def edit_page(request, show_id):
    context = {
        "show": Shows.objects.get(id=show_id),
    }
    return render (request, "tv_show_app/edit.html", context)


    # edit_show = Shows.objects.get(id=show_id)
    # edit_show.title = request.POST["edit_title"]
    # edit_show.network = request.POST["network"]
    # edit_show.release_date = request.POST["release_date"]

def destroy(request, show_id):
    Shows.objects.get(id = show_id).delete()
    return redirect ("/shows")
