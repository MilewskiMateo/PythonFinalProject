# AUTO GENERATED FILE - DO NOT EDIT

''PlayComponent <- function(id=NULL, value=NULL) {
    
    props <- list(id=id, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PlayComponent',
        namespace = 'custom_play_component',
        propNames = c('id', 'value'),
        package = 'customPlayComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
