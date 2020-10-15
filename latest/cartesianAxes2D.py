#!/usr/bin/python

# --------------------------------------------------------------------------------------
#
#    cartesianAxes2D: - Inkscape extension to assist creating 2D cartesian axes
#
#    Copyright (C) 2016 by Fernando Moura
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# --------------------------------------------------------------------------------------

import math

import inkscapeMadeEasy.inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy.inkscapeMadeEasy_Plot as inkPlot


# ---------------------------------------------


class AxisCartesian(inkBase.inkscapeMadeEasy):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.arg_parser.add_argument("--tab", type=str, dest="tab", default="object")

        self.arg_parser.add_argument("--xMin", type=float, dest="xMin", default=-2.0)
        self.arg_parser.add_argument("--xMax", type=float, dest="xMax", default=2.0)
        self.arg_parser.add_argument("--xLabel", type=str, dest="xLabel", default='')
        self.arg_parser.add_argument("--xScale", type=float, dest="xScale", default=5)
        self.arg_parser.add_argument("--xLog10scale", type=self.bool, dest="xLog10scale", default=False)
        self.arg_parser.add_argument("--xTicks", type=self.bool, dest="xTicks", default=False)
        self.arg_parser.add_argument("--xTickStep", type=float, dest="xTickStep", default=1)
        self.arg_parser.add_argument("--xGrid", type=self.bool, dest="xGrid", default=True)
        self.arg_parser.add_argument("--xExtraText", type=str, dest="xExtraText", default='')

        self.arg_parser.add_argument("--yMin", type=float, dest="yMin", default=-2.0)
        self.arg_parser.add_argument("--yMax", type=float, dest="yMax", default=2.0)
        self.arg_parser.add_argument("--yLabel", type=str, dest="yLabel", default='')
        self.arg_parser.add_argument("--yScale", type=float, dest="yScale", default=5)
        self.arg_parser.add_argument("--yLog10scale", type=self.bool, dest="yLog10scale", default=False)
        self.arg_parser.add_argument("--yTicks", type=self.bool, dest="yTicks", default=False)
        self.arg_parser.add_argument("--yTickStep", type=float, dest="yTickStep", default=1)
        self.arg_parser.add_argument("--yGrid", type=self.bool, dest="yGrid", default=True)
        self.arg_parser.add_argument("--yExtraText", type=str, dest="yExtraText", default='')

        self.arg_parser.add_argument("--generalAspectFactor", type=float, dest="generalAspectFactor", default=1.0)

    def effect(self):
        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.svg.namedview.center[0], self.svg.namedview.center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        # root_layer = self.current_layer
        root_layer = self.document.getroot()
        # root_layer = self.getcurrentLayer()

        Xlimits = [so.xMin, so.xMax]
        Ylimits = [so.yMin, so.yMax]

        # defines text height and line width
        textSize = so.generalAspectFactor * 0.25 * min(so.xScale, so.yScale)
        lineWidthAxis = so.generalAspectFactor * min(so.xScale, so.yScale) / 35.0

        inkPlot.axis.cartesian(self, root_layer, Xlimits, Ylimits, position, xLabel=so.xLabel, yLabel=so.yLabel, xlog10scale=so.xLog10scale,
                               ylog10scale=so.yLog10scale, xTicks=so.xTicks, yTicks=so.yTicks, xTickStep=so.xTickStep, yTickStep=so.yTickStep,
                               xScale=so.xScale, yScale=so.yScale, xAxisUnitFactor=so.xExtraText, yAxisUnitFactor=so.yExtraText, xGrid=so.xGrid,
                               yGrid=so.yGrid, forceTextSize=textSize, forceLineWidth=lineWidthAxis)


if __name__ == '__main__':
    axis = AxisCartesian()
    axis.run()
