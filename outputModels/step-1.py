from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
import os
#os.chdir(r"G:\Abaqus_calc_2022\PSCT\data")

name = "F:/Program/Abaqus_Downloads/SIMULIA/rsrs/AISI304/10x20x70/u0/10x20x70-u=0-4.odb"
o3 = session.openOdb(
    name= name)
#: Model: G:/Abaqus_calc_2022/PSCT/data/Test_PSCT_aisi_304_1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       4
#: Number of Node Sets:          9
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
odb = session.odbs[name]
session.xyDataListFromField(odb=odb, outputPosition=NODAL, variable=(('COORD',
    NODAL), ('RF', NODAL), ('PE', INTEGRATION_POINT), ('PEEQ',
    INTEGRATION_POINT), ('S', INTEGRATION_POINT), ), nodeSets=(
    "ANVIL-1.RP_MOVE", ))
odb = session.odbs[name]
xy_result = session.XYDataFromHistory(
    name='CAREA on surface ASSEMBLY_BILLET-1_FOR_CONTACT-1', odb=odb,
    outputVariableName='Total area in contact: CAREA on surface ASSEMBLY_BILLET-1_FOR_CONTACT',
    steps=('Step-1', ), __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy_result)

if 'XYPlot-1' in session.xyPlots.keys():
    del session.xyPlots['XYPlot-1']

xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
x0 = session.xyDataObjects['CAREA on surface ASSEMBLY_BILLET-1_FOR_CONTACT-1']
x1 = session.xyDataObjects['COORD:COOR1 PI: ANVIL-1 N: 1']
x2 = session.xyDataObjects['COORD:COOR2 PI: ANVIL-1 N: 1']
x3 = session.xyDataObjects['COORD:COOR3 PI: ANVIL-1 N: 1']
x4 = session.xyDataObjects['COORD:Magnitude PI: ANVIL-1 N: 1']
x5 = session.xyDataObjects['RF:Magnitude PI: ANVIL-1 N: 1']
x6 = session.xyDataObjects['RF:RF1 PI: ANVIL-1 N: 1']
x7 = session.xyDataObjects['RF:RF2 PI: ANVIL-1 N: 1']
x8 = session.xyDataObjects['RF:RF3 PI: ANVIL-1 N: 1']
session.writeXYReport(fileName='PSCT_data_output' + name.split('/')[-1] + '.rpt', xyData=(x0, x1, x2, x3, x4, x5, x6, x7, x8))
