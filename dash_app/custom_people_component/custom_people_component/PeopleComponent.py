# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class PeopleComponent(Component):
    """A PeopleComponent component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- names (list of strings; optional):
    The max number of pages.

- value (string; optional):
    The value displayed in the input."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, names=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'names', 'value']
        self._type = 'PeopleComponent'
        self._namespace = 'custom_people_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'names', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(PeopleComponent, self).__init__(**args)
