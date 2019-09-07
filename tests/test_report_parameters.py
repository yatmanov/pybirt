import lxml.html
import pytest

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


@pytest.fixture
def empty_scalar():
    return lxml.html.fromstring('<scalar-parameter name="NewParameter3" id="145"></scalar-parameter>')


def test_scalar_parameter_all_attributes_are_optional(empty_scalar):
    ScalarParameter.build(empty_scalar)


def test_is_required_by_default_is_true(empty_scalar):
    assert ScalarParameter.build(empty_scalar).is_required


def test_is_hidden_by_default_is_false(empty_scalar):
    assert ScalarParameter.build(empty_scalar).is_hidden is False


def test_scalar_parameter():
    name = 'OrderNumber'
    description = 'Order number for the invoice'
    data_type = 'string'
    display_format = 'text-box'
    el = lxml.html.fromstring(
        f'<scalar-parameter name="{name}" id="5">'
        f'    <text-property name="displayName">Order Number</text-property>'
        f'    <property name="hidden">true</property>'
        f'    <text-property name="helpText">{description}</text-property>'
        f'    <text-property name="promptText">rrstdstd</text-property>'
        f'    <property name="valueType">static</property>'
        f'    <property name="isRequired">false</property>'
        f'    <property name="dataType">{data_type}</property>'
        f'    <property name="distinct">true</property>'
        f'    <simple-property-list name="defaultValue">'
        f'        <value type="constant">rsh</value>'
        f'    </simple-property-list>'
        f'    <list-property name="selectionList"/>'
        f'    <property name="paramType">simple</property>'
        f'    <property name="controlType">{display_format}</property>'
        f'    <structure name="format">'
        f'        <property name="category">Unformatted</property>'
        f'    </structure>'
        f'</scalar-parameter>'
    )
    sc = ScalarParameter.build(el)
    assert sc.name == name
    assert sc.description == description
    assert sc.data_type == data_type
    assert sc.display_format == display_format
    assert sc.is_required is False
    assert sc.is_hidden
