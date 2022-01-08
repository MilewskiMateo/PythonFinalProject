import React, {Component,useEffect} from 'react';
import PropTypes from 'prop-types';
//import {element as Yellow} from '../../images/personYellow.png';
//import {element as Blue} from '../../images/personBlue.png';
import AvatarSVG from '../../images/person.svg';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const PeopleComponent = ({id, names, setProps, value}) => {
        return (
            <div id='choose_person_wrapper'>
                {names.map(name =>
                <button className='person' disabled={value === 0 } onClick={( e => setProps({ value: name }))}>
                <AvatarSVG id="avatar" style={value === name ? {fill: "#FFd15f" ,width: '70%'}: {fill: "#4C78A8", width: '70%'} } />
                <div style={{color: '#95969A', fontSize: '20px'}}> {name} </div>
                </button>
                )}
            </div>
        );

}

PeopleComponent.defaultProps = {};

PeopleComponent.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

     /**
     * The max number of pages.
     */
    names: PropTypes.arrayOf(PropTypes.string),

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default PeopleComponent