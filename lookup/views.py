from django.shortcuts import render

def home(request):
    import json
    import requests

    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F3ECAC13-90C4-4ADD-93D3-7284B0A5138A")


    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
   
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
