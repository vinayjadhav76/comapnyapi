from django.http import HttpResponse,JsonResponse

def home_page(request):
    frinds=['Vinay','Ketan','Gangaram',"Abhilash" ]
    # return HttpResponse("This is home page",frinds)
    return JsonResponse(frinds, safe=False)