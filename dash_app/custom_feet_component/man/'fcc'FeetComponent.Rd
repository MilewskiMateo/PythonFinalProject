% Auto-generated: do not edit by hand
\name{'fcc'FeetComponent}

\alias{'fcc'FeetComponent}

\title{FeetComponent component}

\description{
Custom component for displaying sensors position on the feet and their current value
}

\usage{
'fcc'FeetComponent(id=NULL, className=NULL, height=NULL, sensorValues=NULL,
width=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{className}{Character. CSS classes added to the main div}

\item{height}{Numeric. Height of the component in px}

\item{sensorValues}{List of numerics. Feet pressure sensor values}

\item{width}{Numeric. Width of the component in px}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

