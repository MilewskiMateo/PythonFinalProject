# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FeetComponent(Component):
    """A FeetComponent component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- className (string; optional):
    CSS classes added to the main div.

- height (number; default 350):
    Height of the component in px.

- sensorValues (list of numbers; default [0, 0, 0, 0, 0, 0]):
    Feet pressure sensor values.

- width (number; default 350):
    Width of the component in px."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, sensorValues=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'height', 'sensorValues', 'width']
        self._type = 'FeetComponent'
        self._namespace = 'custom_feet_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'height', 'sensorValues', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FeetComponent, self).__init__(**args)
