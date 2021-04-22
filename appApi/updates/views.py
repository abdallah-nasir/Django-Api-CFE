from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
from .models import *
from .mixins import JsonResponseMixin,CSRFexempt,AjaxFormMixin
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# def detail(request):
#     # URI -- uniform resorces identifier REST Api
#     data={
#         "user":100,
#         "content":100,
#         "timestamp":100,
#     }
#     return JsonResponse(data)

#     # same with CBV
# class JsonCbv1(JsonResponseMixin,CSRFexempt,View):
#     def get(self,request,*args,**kwargs):
#         # obj=Update.objects.get(id=1)
#         obj=Update.objects.all().serialize()
#         return HttpResponse(obj,content_type="application/json")


# class JsonCbv2(JsonResponseMixin,CSRFexempt,View):
#     def get(self,request,*args,**kwargs):
#         obj=Update.objects.get(id=1).serialize()
#         return HttpResponse(obj,content_type="application/json")




# yourapp.views.py

from django.views.generic import FormView

from .forms import JoinForm


# from step 2

from django.http import JsonResponse

# class JoinFormView(AjaxFormMixin,FormView):
#     form_class = JoinForm
#     template_name  = 'ajax.html'
#     success_url="/success/"
#     def form_invalid(self, form):
#         response = super(JoinFormView, self).form_invalid(form)
#         if self.request.is_ajax():
#             print("Failed")
#             return JsonResponse(form.errors, status=400)
#         else:
#             return response

#     def form_valid(self, form):
#         response = super(JoinFormView, self).form_valid(form)
#         if self.request.is_ajax():
#             print(form.cleaned_data)
#             data = {
#                 'message': "Successfully submitted form data."
#             }
#             return JsonResponse(data)
#         else:
#             return response

def JoinFormView(request):
    form=JoinForm(request.POST or None,request.FILES or None)
    if request.is_ajax():
        Update.objects.create(user=request.user,content="asdasd")
        data = {
                'message': "Successfully submitted form data."
        }
        return JsonResponse(data)
    context={"form":form}
    return render(request,"ajax.html",context)
















