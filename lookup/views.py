from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=F3ECAC13-90C4-4ADD-93D3-7284B0A5138A")
    #89129
    #30103
    #website to generate json=https://docs.airnowapi.org/CurrentObservationsByZip/query

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 - 50 Air quality is good"
            category_color = "good"
        elif api[0]['Category']['Name']  == "Moderate":
            category_description = "51 - 100 Air quality is moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150 Air quality is unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 - 200 Air quality is unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 - 300 Air quality is poor"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "301+ Air quality is hazardous"
            category_color = "hazardous"
    
        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color,
            })
    
    else:

        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=30103&distance=5&API_KEY=F3ECAC13-90C4-4ADD-93D3-7284B0A5138A")
    #89129
    #30103

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 - 50 Air quality is good"
            category_color = "good"
        elif api[0]['Category']['Name']  == "Moderate":
            category_description = "51 - 100 Air quality is moderate"
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150 Air quality is unhealthy for Sensitive Groups"
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 - 200 Air quality is unhealthy"
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "201 - 300 Air quality is poor"
            category_color = "veryunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "301+ Air quality is hazardous"
            category_color = "hazardous"
    
        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color,
            })

def about(request):
    return render(request, 'about.html', {})