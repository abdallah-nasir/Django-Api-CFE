from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



class JsonResponseMixin(object):
    def render_to_json_response(self,context,**response_kwargs):
        return JsonResponse(self.get_data(context),**response_kwargs)

    def get_data(self,context):
        return context 
        #above this is to take the cotext and transform ot to json (overwrite)

class CSRFexempt(object):
    @method_decorator(csrf_exempt)
    def dispatch(self,*args,**kwargs):
        return super().dispatch(*args,**kwargs)


# yourapp.mixins.py

class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            print(form.cleaned_data)
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data)
        else:
            return response
    