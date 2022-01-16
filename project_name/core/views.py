from django.shortcuts import render


def index(request):
    template_name = "core/index.html"
    context = dict(
        text="Hello World!",
    )
    return render(request, template_name, context=context)
