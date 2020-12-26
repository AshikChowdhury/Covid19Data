from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
    'x-rapidapi-key': "9a0bbe1344msh46654ee02f67814p17e7f4jsnf46a4cc9f999",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers).json()


# Create your views here.
def helloWorldview(request):
    noofresults = int(response['results'])
    country_list = []
    for x in range(0, noofresults):
        country_list.append(response['response'][x]['country'])
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry, 'country_list': country_list,
                   'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered,
                   'deaths': deaths, 'total': total,
                   }
        return render(request, 'helloworld.html', context)
    noofresults = int(response['results'])
    country_list = []
    for x in range(0, noofresults):
        country_list.append(response['response'][x]['country'])
    context = {'country_list': country_list}
    return render(request, 'helloworld.html', context)
