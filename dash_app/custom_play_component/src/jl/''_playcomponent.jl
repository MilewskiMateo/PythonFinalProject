# AUTO GENERATED FILE - DO NOT EDIT

export ''_playcomponent

"""
    ''_playcomponent(;kwargs...)

A PlayComponent component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `value` (Bool; optional): The value displayed in the input.
"""
function ''_playcomponent(; kwargs...)
        available_props = Symbol[:id, :value]
        wild_props = Symbol[]
        return Component("''_playcomponent", "PlayComponent", "custom_play_component", available_props, wild_props; kwargs...)
end

