height=300
width=672
labelFontSize=15
titleFontSize=20 # axis title font size
fontSize=25 # title font size
textFontSize=22

# level 3
color='#636466'
color2 = ['#636466','#80C11E']
iColor2 = ['#80C11E','#636466']


def configure_layout(chart):
    return chart.configure_axis(
        labelFontSize=labelFontSize,
        titleFontSize=titleFontSize
    ).configure_title(fontSize=fontSize)