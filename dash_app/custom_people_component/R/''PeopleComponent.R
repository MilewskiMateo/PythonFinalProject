# AUTO GENERATED FILE - DO NOT EDIT

''PeopleComponent <- function(id=NULL, names=NULL, value=NULL) {
    
    props <- list(id=id, names=names, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'PeopleComponent',
        namespace = 'custom_people_component',
        propNames = c('id', 'names', 'value'),
        package = 'customPeopleComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
