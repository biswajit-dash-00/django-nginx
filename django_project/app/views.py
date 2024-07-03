from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("""<body style="height: 100vh;width: 100vw;text-align: center;background-color: black;color: aliceblue;">
    <h1>Hello World !</h1>
    <h3>This page is for Django, Nginx with Docker.</h3>
</body>""")