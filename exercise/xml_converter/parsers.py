from rest_framework_xml.parsers import XMLParser


class XMLApolloParser(XMLParser):
    """
    This parser overrides the behavior of XMLParser from django rest framework.
    """

    def _xml_convert(self, element):
        """
        Convert the xml `element` into the corresponding python object.
        """
        children = list(element)

        if len(children) == 0:
            text = element.text if element.text else ''
            return {element.tag: text}
        else:
            data = {}
            sub_elements = []
            for child in children:
                sub_elements.append(self._xml_convert(child))
            data[element.tag] = sub_elements
        return data
