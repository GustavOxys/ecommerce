
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse



class Pay(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pay')


class CompleteOrder(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Complete Order')


class Detail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detail')
