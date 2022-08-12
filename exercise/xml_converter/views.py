from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from rest_framework.exceptions import ParseError
from xml_converter.forms import UploadFileForm
from xml_converter.parsers import XMLApolloParser


def upload_page(request):
    if request.method == 'POST':
        xml_file = request.FILES['file']
        try:
            converted = XMLApolloParser().parse(xml_file)
        except ParseError:
            return HttpResponseBadRequest()
        return JsonResponse(converted)
    form = UploadFileForm()
    return render(request, "upload_page.html", {"form": form})
