import contextlib
import dataclasses
from typing import List

import lxml.html

__all__ = ['ScalarParameter', 'ParameterGroup']


@dataclasses.dataclass
class ScalarParameter:
    name: str
    description: str
    data_type: str
    display_format: str
    is_required: bool
    is_hidden: bool

    @classmethod
    def build(cls, element: lxml.html.HtmlElement) -> 'ScalarParameter':
        _properties = []
        for xpath in ('./text-property[@name="displayName"]',
                      './property[@name="dataType"]',
                      './property[@name="controlType"]',
                      ):
            try:
                _properties.append(element.xpath(xpath)[0].text)
            except (IndexError, AttributeError):
                _properties.append('')
        required_el = element.xpath('./property[@name="isRequired"]')
        hidden_el = element.xpath('./property[@name=hidden]')

        return cls(
            element.attrib['name'],
            *_properties,
            required_el[0].text == 'true' if required_el else True,
            hidden_el[0].text == 'true' if hidden_el else False,
        )


@dataclasses.dataclass
class ParameterGroup:
    name: str
    display_name: str
    parameters: List[ScalarParameter] = dataclasses.field(default_factory=list)

    @classmethod
    def build(cls, el: lxml.html.HtmlElement) -> 'ParameterGroup':
        _el = el.xpath('./text-property[name="displayName"]')

        params = el.xpath('./parameters')
        childs = []
        if params:
            for child in params[0].iterchildren():
                if child.tag == 'parameter-group':
                    childs.append(ParameterGroup.build(child))
                elif child.tag == 'scalar-parameter':
                    with contextlib.suppress(Exception):
                        childs.append(ScalarParameter.build(child))

        return cls(el.get('name', 'root'), _el[0].text if _el else '', childs)
