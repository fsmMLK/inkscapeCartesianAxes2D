# cartesianAxes2D
Inkscape extension to assist creating 2D Cartesian axes


<img src="docs/images/Examples.png" width="900px"/>

### main features

The main features are

 - linear and log10 scales
 - optional grid lines in X and Y directions
 - adjustable tick mark intervals and sizes
 - LaTeX support

# Installation and requirements

This extension was partially developed in Inkscape 0.48 and partially in 0.91 in Linux (Kubuntu 12.04 and 14.04). It should work on both versions of Inkscape. Also, they should work in different OSs too as long as all requirements are installed.

This extension requires another extension to run, inkscapeMadeEasy <https://github.com/fsmMLK/inkscapeMadeEasy>, which contains several backstage methods and classes.

In order to use cartesianAxes2D extension, you must also download inkscapeMadeEasy files and put them inside Inkscape's extension directory. Please refer to inkscapeMadeEasy installation instructions. In the end you must have the following files and directories in your Inkscape extension directory.

```
inkscape/extensions/
            |-- inkscapeMadeEasy_Base.py
            |-- inkscapeMadeEasy_Draw.py
            |-- inkscapeMadeEasy_Plot.py
            |-- textextLib
            |   |-- __init__.py
            |   |-- basicLatexPackages.tex
            |   |-- textext.inx
            |   |-- textext.py
            |
            |-- cartesianAxes2D.py
            `-- cartesianAxes2D.inx
```

# Usage

This extension is presented in two tabs, **Xaxis** and  **Yaxis**. They are used to configure independently the axes of your Cartesian plot. Both tabs have the same control elements, with the exception of the last control in the Xaxis tab, which controls the general aspect ratio of the Cartesian axis.

**X/Y axis label:** label of the axes. This string must be LaTeX compatible. Any LaTeX commands or environments are valid. If you want to write in mathematical environment, enclose your text with $...$. You don't have to escape any backslashes.

> Tip: Since `siunitx` package is included in basicLatexPackages.tex file by default in inkscapeMadeEasy, you can use any unit command available there 

Ex: `Foobar $\sqrt{x^2}$ so fancy! (\si{\newton\per\squaremetre})`

<img src="docs/images/Legend_01.png" width="400px"/>

**X/Y min and max:** Set the limits of the axes. The extension will inform if these limits are invalid.
  
  - The upper limit must be greater than the lower limit
  - If logarithmic scale is checked, then the limits must be positive
  - If logarithmic scale is checked, then the lower limit will be rounded down to the nearest power of 10 and the upper rounded up to the nearest power of 10 in order to complete the decades. Ex: 0.2 to 12, then the limits will be rounded to 0.1 to 100

**Logarithmic scale:** Set the axis to be represented in log10 scale. In such case, the limits of the axis must be both greater than zero.

**Add grid to X/Y axis:** Draw grid lines in X or Y axes.
   - *linear scale:* The grid lines will be placed at each tick marks
   - *logarithmic scale:* The grid lines will be placed dividing each decade in 10 parts in at each tick marks

**X/Y tick step:** Tick marks interval in plot units. This value is not referenced to  in logarithmic scale

Ex: limits from -1 to 1, with tick step of 0.5 will produce ticks at -1, -0.5, 0, 0.5, 1

> Note: The ticks will radiate from the origin x=0 or y=0 unless the origin does not lie within the limits. In such cases, the ticks will radiate starting from the  limit closest to the origin.
>
> Examples
> <img src="docs/images/TickStep.png" width="600px"/>


**X/Y tick length** The distance between the tick marks, in px.
   - *linear scale:* The distance between ticks in px.
   - *logarithmic scale:* The size of each decade in px.

<img src="docs/images/TickLength.png" width="350px"/>

**X/Y tick suffix value:** Optional extra suffix to the added to the tick values. You can use any LaTeX text/commands valid in mathematical environment $...$. You don't have to enclose your text between $...$. You don't have to escape any backslashes.

<img src="docs/images/TickSuffix.png" width="800px"/>

**General aspect factor:** (present in Xaxis tab only) General aspect ratio between line width and text width. I designed this extension to have an overall
  aspect ratio that looked nice to my eyes. It is a function of X and Y tick lengths. With this control you can scale both line widths and text height to fit your needs.

<img src="docs/images/generalAspectRatio.png" width="700px"/>

# Observations

 - The axes will be placed crossing the origin (0,0) or crossing the coordinate (x,y) closest to the origin if the origin does not lies within the limits.

# Examples

<img src="docs/images/Examples.png" width="900px"/>



