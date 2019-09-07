import lxml.html

from pybirt import ParameterGroup


def test_empty_parameter_group():
    el = lxml.html.fromstring('<parameter-group name="NewParameterGroup1" id="144"/>')
    _ = ParameterGroup.build(el)
