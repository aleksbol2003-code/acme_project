from django.shortcuts import render  # type: ignore


def homepage(request):
    return render(request, 'pages/index.html')
