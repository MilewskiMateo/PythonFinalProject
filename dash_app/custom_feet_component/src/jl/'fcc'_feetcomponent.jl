# AUTO GENERATED FILE - DO NOT EDIT

export 'fcc'_feetcomponent

"""
    'fcc'_feetcomponent(;kwargs...)

A FeetComponent component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `className` (String; optional): CSS classes added to the main div
- `height` (Real; optional): Height of the component in px
- `sensorValues` (Array of Reals; optional): Feet pressure sensor values
- `width` (Real; optional): Width of the component in px
"""
function 'fcc'_feetcomponent(; kwargs...)
        available_props = Symbol[:id, :className, :height, :sensorValues, :width]
        wild_props = Symbol[]
        return Component("'fcc'_feetcomponent", "FeetComponent", "custom_feet_component", available_props, wild_props; kwargs...)
end

