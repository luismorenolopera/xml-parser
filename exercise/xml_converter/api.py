from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from xml_converter.parsers import XMLApolloParser


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        xml_file = request.FILES['file']
        try:
            converted = XMLApolloParser().parse(xml_file)
        except ParseError:
            raise ParseError
        return Response(converted)
