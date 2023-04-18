height=300
width=672
labelFontSize=15
titleFontSize=20 # axis title font size
fontSize=25 # title font size
textFontSize=22
offset=25

# level 3
color='#636466'
iColor='#80C11E'
color2 = ['#636466','#80C11E']
color6 = ['#636466','#80C11E', '#D8519E', '#E37A45','#773B9A','#E6CB03']
iColor2 = ['#80C11E','#636466']


def configure_layout(chart):
    return chart.configure_axis(
        labelFontSize=labelFontSize,
        titleFontSize=titleFontSize
    ).configure_title(fontSize=fontSize,offset=offset
    ).configure_legend(titleFontSize=titleFontSize, labelFontSize=labelFontSize) 