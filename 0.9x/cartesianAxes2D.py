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

import inkex
import inkscapeMadeEasy_Base as inkBase
import inkscapeMadeEasy_Draw as inkDraw
import inkscapeMadeEasy_Plot as inkPlot
import math

#---------------------------------------------


class AxisCartesian(inkBase.inkscapeMadeEasy):
    def __init__(self):
        inkBase.inkscapeMadeEasy.__init__(self)

        self.OptionParser.add_option("--tab", action="store", type="string", dest="tab", default="object")

        self.OptionParser.add_option("--xMin", action="store", type="float", dest="xMin", default=-2.0)
        self.OptionParser.add_option("--xMax", action="store", type="float", dest="xMax", default=2.0)
        self.OptionParser.add_option("--xLabel", action="store", type="string", dest="xLabel", default='')
        self.OptionParser.add_option("--xScale", action="store", type="float", dest="xScale", default=5)
        self.OptionParser.add_option("--xLog10scale", action="store", type="inkbool", dest="xLog10scale", default=False)
        self.OptionParser.add_option("--xTicks", action="store", type="inkbool", dest="xTicks", default=False)
        self.OptionParser.add_option("--xTickStep", action="store", type="float", dest="xTickStep", default=1)
        self.OptionParser.add_option("--xGrid", action="store", type="inkbool", dest="xGrid", default=True)
        self.OptionParser.add_option("--xExtraText", action="store", type="string", dest="xExtraText", default='')

        self.OptionParser.add_option("--yMin", action="store", type="float", dest="yMin", default=-2.0)
        self.OptionParser.add_option("--yMax", action="store", type="float", dest="yMax", default=2.0)
        self.OptionParser.add_option("--yLabel", action="store", type="string", dest="yLabel", default='')
        self.OptionParser.add_option("--yScale", action="store", type="float", dest="yScale", default=5)
        self.OptionParser.add_option("--yLog10scale", action="store", type="inkbool", dest="yLog10scale", default=False)
        self.OptionParser.add_option("--yTicks", action="store", type="inkbool", dest="yTicks", default=False)
        self.OptionParser.add_option("--yTickStep", action="store", type="float", dest="yTickStep", default=1)
        self.OptionParser.add_option("--yGrid", action="store", type="inkbool", dest="yGrid", default=True)
        self.OptionParser.add_option("--yExtraText", action="store", type="string", dest="yExtraText", default='')

        self.OptionParser.add_option("--generalAspectFactor", action="store", type="float", dest="generalAspectFactor", default=1.0)

    def effect(self):

        so = self.options

        # sets the position to the viewport center, round to next 10.
        position = [self.view_center[0], self.view_center[1]]
        position[0] = int(math.ceil(position[0] / 10.0)) * 10
        position[1] = int(math.ceil(position[1] / 10.0)) * 10

        #root_layer = self.current_layer
        root_layer = self.document.getroot()
        #root_layer = self.getcurrentLayer()

        Xlimits = [so.xMin, so.xMax]
        Ylimits = [so.yMin, so.yMax]

        #defines text height and line width
        textSize = so.generalAspectFactor * 0.25 * min(so.xScale, so.yScale)
        lineWidthAxis = so.generalAspectFactor * min(so.xScale, so.yScale) / 35.0

        inkPlot.axis.cartesian(self, root_layer, Xlimits, Ylimits, position, xLabel=so.xLabel, yLabel=so.yLabel,
                               xlog10scale=so.xLog10scale, ylog10scale=so.yLog10scale,
                               xTicks=so.xTicks, yTicks=so.yTicks, xTickStep=so.xTickStep, yTickStep=so.yTickStep,
                               xScale=so.xScale, yScale=so.yScale, xAxisUnitFactor=so.xExtraText, yAxisUnitFactor=so.yExtraText,
                               xGrid=so.xGrid, yGrid=so.yGrid, forceTextSize=textSize, forceLineWidth=lineWidthAxis)


if __name__ == '__main__':
    axis = AxisCartesian()
    axis.affect()
