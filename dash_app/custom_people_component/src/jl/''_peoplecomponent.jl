# AUTO GENERATED FILE - DO NOT EDIT

export ''_peoplecomponent

"""
    ''_peoplecomponent(;kwargs...)

A PeopleComponent component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `names` (Array of Strings; optional): The max number of pages.
- `value` (String; optional): The value displayed in the input.
"""
function ''_peoplecomponent(; kwargs...)
        available_props = Symbol[:id, :names, :value]
        wild_props = Symbol[]
        return Component("''_peoplecomponent", "PeopleComponent", "custom_people_component", available_props, wild_props; kwargs...)
end

