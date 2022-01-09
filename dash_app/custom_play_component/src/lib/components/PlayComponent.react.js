import React, {Component,useEffect} from 'react';
import PropTypes from 'prop-types';
//import {element as Yellow} from '../../images/personYellow.png';
//import {element as Blue} from '../../images/personBlue.png';
import PlaySVG from '../../images/play.svg';
import PauseSVG from '../../images/pause.svg';
/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const PlayComponent = ({id, setProps, value}) => {

        return (
                <button className='play_button' onClick={( e => setProps({ value: !value  }))}>
                    {value ? 
                    <PlaySVG className="play_svg" style={{fill: "#4C78A8", width: '70%', height: '70%'}} />
                    : <PauseSVG className="pause_svg" style={{fill: "#4C78A8", width: '70%',height: '70%'}}/> }
                </button>
        );

}

PlayComponent.defaultProps = {};

PlayComponent.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.bool,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default PlayComponent