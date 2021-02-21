from bpy import ops,data,context
from math import pi, atan2,cos,sin

def deleteAll():
    ops.object.select_all(action='DESELECT')
    for object in data.objects:
        object.select_set(True)
        ops.object.delete()
    for material in data.materials:
        material.user_clear()
        data.materials.remove(material)

def HSV2RGB(H,S,V=1):
    C = V*S
    X = C*(1-abs((H/60)%2 - 1))
    m = V-C
    if H <60:
        RGB_dash = [C,X,0]
    elif H<120:
        RGB_dash = [X,C,0]
    elif H<180:
        RGB_dash = [0,C,X]
    elif H<240:
        RGB_dash = [0,X,C]
    elif H<300:
        RGB_dash = [X,0,C]
    else:
        RGB_dash = [C,0,X]
    Rd,Gd,Bd = RGB_dash
    return [(Rd+m),(Gd+m),(Bd+m)]

def makeFibre(ele, azi,sectionRad = 0.02,fibreName = 'Fibre'):
    #bezier curve controls cross section of the fibre for visualisation, zero in reality
    ops.curve.primitive_bezier_circle_add()
    fibreCrossSec = data.objects['BezierCircle']
    fibreCrossSec.name = fibreName +'_fibreCrossSec'
    
    if ele == pi:
        fibreCrossSec.scale = [sectionRad,sectionRad,1]
        ops.curve.primitive_nurbs_path_add()
        fibre = data.objects['NurbsPath']
        fibreCurve = data.curves['NurbsPath']
        fibre.rotation_euler.y = pi/2
        fibre.scale.x = 1000
        fibre.data.bevel_object = fibreCrossSec
        new_mat = data.materials.new(name = 'FibreColour')
        new_mat.diffuse_color = (0,0,1,1)
        fibre.data.materials.append(new_mat)
    else:
        ele /= 2
        baseRad = 2*((1/(pi/2 - ele)) - (2/pi))
        fibreRad = baseRad + 1/(baseRad +1)
        fibreCrossSec.scale = [sectionRad/fibreRad,sectionRad/fibreRad,1]
        fibreCentre = (baseRad*sin(azi), baseRad*cos(azi),0)
        ops.curve.primitive_bezier_circle_add()
        fibre = data.objects['BezierCircle']
        fibreCurve = data.curves['BezierCircle']
        fibre.name, fibreCurve.name = (fibreName,fibreName)
        fibre.location = fibreCentre
        fibre.scale = (fibreRad,fibreRad,fibreRad)
        fibre.rotation_euler.y = ele
        fibre.rotation_euler.z = -azi 
        fibre.data.bevel_object = fibreCrossSec
        new_mat = data.materials.new(name = 'FibreColour')
        hue = (azi*15/pi) + ele*330/pi
        r,g,b = HSV2RGB(hue,1,1)
        #print(hue)
        new_mat.diffuse_color = (r,g,b,1)
        fibre.data.materials.append(new_mat)
    ops.object.select_all(action='DESELECT')

def main():
    deleteAll()
    context.scene.cursor.location = (0.0, 0.0, 0.0)
    
    tori = 6
    fibresPerTorus = 50 
    section = 0.8
    elevationRange = [(e+1)*pi/tori for e in range(tori)][:-1]
    azimuthRange = [(a*2*pi*section)/fibresPerTorus for a in range(fibresPerTorus)]
    
    for ele in elevationRange:
        for azi in azimuthRange:
            makeFibre(ele,azi,fibreName = 'Fibre_{}_{}'.format(ele,azi))
    makeFibre(0,0,fibreName = 'Fibre_0_0')
    makeFibre(pi,0,fibreName='Fibre_{}_0'.format(pi))


if __name__ == '__main__':
    main()
    
    
