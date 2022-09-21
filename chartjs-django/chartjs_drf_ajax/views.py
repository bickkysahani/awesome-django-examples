from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

class IndexView(TemplateView):
    template_name = 'index.html'

class ChartData(APIView):

    def get(self, request, format=None):
        #labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        chartdata  = [12, 19, 3, 5, 2, 3]
        chartdata2  = [55, 9, 30, 15, 8, 33]
        chartLabel = '# of Votes'
        chartLabel2 = '# of Votes2'
        data = {
                "labels":  ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                "chartdata": chartdata,
                "chartdata2": chartdata2,
                "chartLabel": chartLabel,
                "chartLabel2": chartLabel2,
        }
        return Response(data)