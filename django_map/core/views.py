from django.shortcuts import render


def main(request):
    template = 'core/main.html'
    return render(request, template)
