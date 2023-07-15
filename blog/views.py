from django.shortcuts import render
from django.views import View
from .models import Enquery
from django.http import JsonResponse

def Home(request):
    return render(request, 'index.html')


class Contact(View):
    def get(self, request):
        data = {}
        data['enquiries'] = Enquery.objects.all().order_by('created_at')
        print(data)
        return render(request, 'contact.html', data)
    
    def post(self, request):
        try:
            cat = Enquery()
            cat.name = request.POST.get('name')
            cat.save()
            data = {'error':False, 'message':'data saved successfully'}
        except Exception as e:
            data = {'error':True, 'message':str(e)}

        return JsonResponse(data)



class ContactEdit(View):
    def get(self, request, id):
        data ={}
        data['cat'] = Enquery.objects.get(id=id)
        print(data)
        return render(request, 'contactEdit.html', data)
    

    def post(self, request, id):
        try:
            en = Enquery.objects.get(id=id)
            en.name = request.POST.get('name')
            en.save()
            data = {'error':True, 'message':'data updated successfully'}
        except Exception as e:
            data = {'error':True, 'message':str(e)}

        return JsonResponse(data)    

    def delete(self, request, id):
        try:
            en = Enquery.objects.get(id=id)
            en.delete()
            data = {'error':True, 'message':'data deleted successfully'}
        except Exception as e:
            data = {'error':True, 'message':str(e)}

        return JsonResponse(data)    







