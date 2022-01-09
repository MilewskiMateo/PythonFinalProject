import React, {useEffect} from 'react';
import PropTypes from 'prop-types';
import FeetSVG from '../../images/feet.svg';
import * as d3 from "d3";

const FeetComponent = ({ id, className, setProps, width, height, sensorValues }) => {
    useEffect(() => {
        const svg = d3.select('#feet-image');
        const wholeImage = svg.select('g');
        const rightFoot = wholeImage.select('path');
        const leftFoot = wholeImage.select('g');

        leftFoot.attr('stroke-width', 1);
        leftFoot.attr('fill', '#FFd15f');
        rightFoot.attr('stroke-width', 1);
        rightFoot.attr('fill', '#FFd15f');
    }, [...sensorValues]);

    useEffect(() => {
        const svg = d3.select('#feet-image');
        const r = 6;

        const positions = [
            { x: 32, y: 33 },
            { x: 10, y: 45 },
            { x: 25, y: 90 },

            { x: 68, y: 33 },
            { x: 90, y: 45 },
            { x: 74, y: 90 },
        ];

        for (const [i, position] of positions.entries()) {
            const { x, y } = position;
            const value = sensorValues[i];

            const g = svg.append('g').classed('sensor-value', true);

            g.append('circle')
                .attr('cx', `${x}%`)
                .attr('cy', `${y}%`)
                .attr('r', `${r}%`)
                .attr('stroke-width', 0.5)
                .style('stroke', '#000000')
                .style('fill', '#4C78A8');

            const transleteY = r * 0.29;
            g.append('text')
                .attr('x', `${x}%`)
                .attr('y', `${y}%`)
                .attr('transform', `translate(0 ${transleteY})`)
                .attr('text-anchor', 'middle')
                .style('font-size', `${r}px`)
                .text(value);
        }

        return () => {
            const svg = d3.select('#feet-image');
            svg.selectAll('.sensor-value').remove();
        }
    }, [...sensorValues]);

    return (
        <div id={id} className={className}>
            <div style={{ width: width, height: height }}>
                <FeetSVG id="feet-image" width={width} height={height} />
            </div>
        </div >
    )
}

FeetComponent.defaultProps = {
    width: 350,
    height: 350,
    sensorValues: [0, 0, 0, 0, 0, 0]
};

FeetComponent.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * CSS classes added to the main div
     */
    className: PropTypes.string,

    /**
     * Width of the component in px
     */
    width: PropTypes.number,

    /**
    * Height of the component in px
    */
    height: PropTypes.number,

    /**
     * Feet pressure sensor values
     */
    sensorValues: PropTypes.arrayOf(PropTypes.number),


    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default FeetComponent;
