from django.shortcuts import render
from django.views.generic import TemplateView

class ListaTesourosView(TemplateView):
    template_name = "lista_tesouros.html"

    def get(self, request):
    	return render(request,
              "lista_tesouros.html",
              {'sobre': [{"titulo":"De onde eles vêm",
                          "texto":"Lorem ipsum dolor sit amet, consectetur"},
                          {"titulo":"O que eles querem",
                          "texto":"osakdpokasdokaspok"},
                          ]})

#    	return render(request,
#              {'lista_tesouros': <Fazer uma busca pelos tesouros>,
 # 				'total_geral': <Somatório do valor de todos os tesouros>
#			  })
#from django.db.models import Count
#Autor.objects.annotate(Count('post'))
