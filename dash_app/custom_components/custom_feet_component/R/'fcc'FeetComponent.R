# AUTO GENERATED FILE - DO NOT EDIT

'fcc'FeetComponent <- function(id=NULL, className=NULL, height=NULL, sensorValues=NULL, width=NULL) {
    
    props <- list(id=id, className=className, height=height, sensorValues=sensorValues, width=width)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FeetComponent',
        namespace = 'custom_feet_component',
        propNames = c('id', 'className', 'height', 'sensorValues', 'width'),
        package = 'customFeetComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
