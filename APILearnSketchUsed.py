#Author-
#Description-

from asyncio import constants
import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
       

        sketch = adsk.fusion.Sketch.cast(app.activeEditObject)
        #sketch: adsk.fusion.Sketch = app.activeEditObject
        
        sketchLines = sketch.sketchCurves.sketchLines
        startPoint = adsk.core.Point3D.create(0,0,0)
        endPoint = adsk.core.Point3D.create(5,5,0)

        sketchLines.addCenterPointRectangle(startPoint,endPoint)
        sketchLines.addByTwoPoints(startPoint,endPoint)
        


        ui.messageBox('Sketch Created')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
