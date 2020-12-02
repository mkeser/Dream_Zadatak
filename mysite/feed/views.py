from django.shortcuts import render

# Create your views here.

tweets = [{"name": "Bud Spencer", "text": "Where is Terence?"},
          {"name": "Terence Hill", "text": "I'm here Bud (pun intended)!"}]


def home(request):
    context = {"tweets": tweets}
    return render(request, "feed/home.html", context)
