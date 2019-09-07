import lxml.html

from pybirt import ParameterGroup


def test_empty_parameter_group():
    el = lxml.html.fromstring('<parameter-group name="NewParameterGroup1" id="144"/>')
    _ = ParameterGroup.build(el)


def test_parameter_group():
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
