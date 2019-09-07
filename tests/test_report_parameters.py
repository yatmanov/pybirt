import lxml.html

from pybirt import ParameterGroup, ScalarParameter


def test_empty_parameter_group():
    el = lxml.html.fromstring('<parameter-group name="NewParameterGroup1" id="144"/>')
    ParameterGroup.build(el)


def test_parameter_group_without_parameters():
    name = 'NewParameterGroup1'
    display_name = 'DisplayName1'
    el = lxml.html.fromstring(
        f'<parameter-group name="{name}" id="144">'
        f'    <text-property name="displayName">{display_name}</text-property>'
        '</parameter-group>'
    )
    group = ParameterGroup.build(el)
    assert group.name == name
    assert group.display_name == display_name
    assert group.parameters == []


def test_scalar_parameter_all_attributes_are_optional():
    el = lxml.html.fromstring(
        '<scalar-parameter name="NewParameter3" id="145">'
        '</scalar-parameter>'
    )
    ScalarParameter.build(el)
