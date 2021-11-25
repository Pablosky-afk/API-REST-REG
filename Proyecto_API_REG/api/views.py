from django.views import View
from .models import registrar
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.

class registrarView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            registros=list(registrar.objets.filter(id=id).values())
            if len(registros)>0:
                #registrar=registros[0]
                print(registros)
            return JsonResponse(datos)
        else:
            registros=list(registrar.objets.values())
            if len(registros)>0:
                datos={'messege':"Success",'registros':registros}
            else:
                datos={'messege':"Registros no encontrados..."}
            return JsonResponse(datos)
        
    def post(self,request):
        jd = json.loads(request.body)
        #print(jd)
        registrar.objets.create(usuario=jd['usuario'],contraseña=jd['contraseña'])
        datos={'messege':"Success"}
        return JsonResponse(datos) 
        

    def putt(self,request,id):
        jd = json.loads(request.body)
        registros=list(registrar.objets.filter(id=id).values())
        if len(registros)>0:
            registrar=registrar.objets.get(id=id)
            registrar.usuario=jd['usuario']
            registrar.contraseña=jd['contraseña']
        else:
            datos={'messege':"Registros no encontrados..."}
        return JsonResponse(datos)

    def delate(self,request,id):
        registros=list(registrar.objets.filter(id=id).values())
        if len(registros)>0:
            registrar.objets.filter(id=id).delate()
            datos={'messege':"Success"}        
        else:
            datos={'messege':"Registros no encontrados..."}
        return JsonResponse(datos)
 

    