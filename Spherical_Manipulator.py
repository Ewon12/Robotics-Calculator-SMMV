import numpy as np
import math
import PySimpleGUI as sg
import pandas as pd

# GUI code
sg.theme('Black')

# Excel Read Code
EXCEL_FILE = 'Spherical  Manipulator - Forward Kinematcs.xlsx'
df = pd.read_excel(EXCEL_FILE)

SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key))

# Layout Code

design = [[sg.Image('spherical modern variant.gif')]]

Main_layout = [
    [sg.Push(),sg.Text('Spherical Manipulator - Modern Variant MEXE CALCULATOR',
     font =("Broadway",20)),sg.Push()],

     [sg.Checkbox('Hide D-H Parametric Table - Spherical Manipulator ', enable_events=True, key='-OPEN SEC1-CHECKBOX')],
     [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), 
        sg.T('D-H Parametric Table - Spherical Manipulator', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(design, '-SEC1-')],


     [sg.Push(),sg.Button('Click This Before Solving Forward Kinematics', tooltip = 'Reset',
    font=("Rockwell Extra Bold",20),size=(20,0),button_color=('red','blue')),sg.Text('OR',font =("Broadway",20)),
    sg.Button('Solve Inverse Kinematics',font=("Rockwell Extra Bold",20),size=(20,0),button_color=('blue','red')),sg.Push()],

    [sg.Push(),sg.Text('Forwad Kinematics Calculator',font=("Cascadia Code",20)),sg.Push()],

    [sg.Push(),sg.Frame('Fill out the following fields:',[
        [sg.Text('a1 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a1',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',10)),
        sg.Text('T1 = ', font = ('Times New Roman',15)),sg.InputText('0',key='T1',size=(15,10)),
        sg.Text('degrees',font = ('Times New Roman',10))],
        [sg.Text('a2 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a2',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',10)),
        sg.Text('T2 = ', font = ('Times New Roman',15)),sg.InputText('0',key='T2',size=(15,10)),
        sg.Text('degrees',font = ('Times New Roman',10))],
        [sg.Text('a3 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a3',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',10)),
        sg.Text('d3 = ', font = ('Times New Roman',15)),sg.InputText('0', key='d3',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',10))],
        [sg.Push(),sg.Button('Solve Forward Kinematics', disabled=True ,font=("Rockwell Extra Bold",15),button_color=('green','blue'))]
        ]),
    
    sg.Frame('H0_3 Transformation Matrix = ', [[sg.Output(size=(60,8))]]),sg.Push()],

    [sg.Push(),sg.Frame('Position Vector :',[[
        sg.Text('X = ', font = ('Times New Roman',10)),sg.InputText(key = 'X',size = (10,1)),sg.Text('mm',font = ('Times New Roman',10)),
        sg.Text('Y = ', font = ('Times New Roman',10)),sg.InputText(key = 'Y',size = (10,1)),sg.Text('mm',font = ('Times New Roman',10)),
        sg.Text('Z = ', font = ('Times New Roman',10)),sg.InputText( key = 'Z',size = (10,1)),sg.Text('mm',font = ('Times New Roman',10))]]),sg.Push()],

    [sg.Push(),
    sg.Frame('Jacobian Matrix:',[[sg.Button('Jacobian Matrix(J)',disabled=True,font=("Elephant",12),size=(12,0),button_color= ('red','white')),
    sg.Button('Det(J)',disabled=True,font=("Elephant",12),size=(12,0),button_color=('green','white')),
    sg.Button('Inverse of J',disabled=True,font=("Elephant",12),size=(12,0),button_color=('blue','white')),
    sg.Button('Transpose of J',disabled=True,font=("Elephant",12),size=(12,0),button_color=('purple','white')),]]),sg.Push()],

    [sg.Frame('Save data', [[
        sg.Submit(tooltip = 'Submit to Excel',font = ('Times New Roman',13)),sg.Exit(font = ('Times New Roman',13))]])]
    
]

opened1 = True

# Window Code
window = sg.Window('Spherical RRP MV MEXE Calculator', Main_layout,resizable =True)

#Inverse Kinematics Function
def Inverse_Kinematics_window():
    sg.theme('Black')

    EXCEL_FILE =  'Spherical Manipulator - Inverse Kinematics.xlsx'
    Ik_df = pd.read_excel(EXCEL_FILE) 

    Ik_layout =[
        [sg.Push(),sg.Text('Inverse Kinematics',font=("Cascadia Code",20)),sg.Push()],
        [sg.Text('a1 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a1',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',15)),sg.Text('X = ', font = ('Times New Roman',15)),
        sg.InputText('0',key='X',size=(15,10)), sg.Text('mm',font = ('Times New Roman',15))],
        [sg.Text('a2 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a2',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',15)),sg.Text('Y = ', font = ('Times New Roman',15)),
        sg.InputText('0',key='Y',size=(15,10)), sg.Text('mm',font = ('Times New Roman',15))],
        [sg.Text('a3 = ', font = ('Times New Roman',15)),sg.InputText('0',key='a3',size=(15,10)),
        sg.Text('mm',font = ('Times New Roman',15)),sg.Text('Z = ', font = ('Times New Roman',15)),
        sg.InputText('0',key='Z',size=(15,10)), sg.Text('mm',font = ('Times New Roman',15))],
        [sg.Push(),sg.Button('Solve Inverse Kinematics', font=("Rockwell Extra Bold",10),
        button_color=('black','pink')),sg.Push()],

        [sg.Frame(' Position Vector Result :',[[
        sg.Text('Theta 1 = ', font = ('Times New Roman',10)),sg.InputText(key = 'Ik_Th1',size = (10,1)),
        sg.Text('degrees',font = ('Times New Roman',10)),
        sg.Text('Theta 2 = ', font = ('Times New Roman',10)),sg.InputText(key = 'Ik_Th2',size = (10,1)),
        sg.Text('degrees',font = ('Times New Roman',10)),
        sg.Text('d3 = ', font = ('Times New Roman',10)),sg.InputText(key = 'Ik_d3',size = (10,1)),
        sg.Text('mm',font = ('Times New Roman',10))]])],

        [sg.Frame('Save data', [[
        sg.Submit(tooltip = 'Submit to Excel',font = ('Times New Roman',13)),sg.Exit(font = ('Times New Roman',13))]])]
    ]

    Inverse_Kinematics_window =sg.Window('Inverse Kinematics',Ik_layout)

    while True:
        event, values = Inverse_Kinematics_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break   

        elif event == 'Solve Inverse Kinematics':

            # Link Lengths in  mm
            a1 = float(values["a1"])
            a2 = float(values["a2"])
            a3 = float(values["a3"])
            
            # Position Vector
            X = float(values["X"])
            Y = float(values["Y"])
            Z = float(values["Z"])

            #Obtain THETA 1 in degrees
            Th1 = np.arctan(Y/X)*180.0/np.pi
            r1 = math.sqrt((X**2)+(Y**2))
            #Obtain THETA 2 in degrees
            r2 = Z - a1
            r3 = math.sqrt((r1**2)+(r2**2))
            d3 = math.sqrt((r3**2)-(a2**2)) - a3
            Pi1 = np.arctan((a3+d3)/a2)*180.0/np.pi
            Pi2 = np.arctan(r2/r1)*180.0/np.pi
            Th2 =  -90.0 + Pi1 + Pi2

            

            Th1 = Inverse_Kinematics_window['Ik_Th1'].Update(np.around(Th1,3))
            Th2 = Inverse_Kinematics_window['Ik_Th2'].Update(np.around(Th2,3))
            d3 = Inverse_Kinematics_window['Ik_d3'].Update(np.around(d3,3))

        elif event == 'Submit':
            Ik_df = df.append(values, ignore_index=True)
            Ik_df.to_excel(EXCEL_FILE, index=False)
            sg.popup('Data saved!')

    Inverse_Kinematics_window.close()


#Variable code for solving disabling button

disable_J= window['Jacobian Matrix(J)']
disable_DetJ = window['Det(J)']
disable_IJ=  window['Inverse of J']
disable_TJ =  window['Transpose of J']
disable_Fk = window['Solve Forward Kinematics']




while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
         sg.popup("Thank You for Using this GUI Apps!!", 'Group 12','Members:','Apolonia, Aaron Joshua', 'Cabrera, Lucky','Dela Dinco, Justin John','Fajardo, Reynalyn' ,'Serrano, Mike Angelo')
         break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-OPEN SEC1-CHECKBOX'].update(not opened1)
        window['-SEC1-'].update(visible=opened1)


    elif event == 'Click This Before Solving Forward Kinematics':
        disable_J.update(disabled =True)
        disable_DetJ.update(disabled =True)
        disable_IJ.update(disabled =True)
        disable_TJ.update(disabled =True)
        disable_Fk.update(disabled =False)
        
        

    elif event == 'Solve Forward Kinematics':
        # Forward Kinematics Codes
        # Link Lengths in
        
        a1 = float(values["a1"])
        a2 = float(values["a2"])
        a3 = float(values["a3"])


        # Joint Variable Theta in degrees
        T1 = float(values["T1"])
        T2 = float(values["T2"])
        d3 = float(values["d3"])

        # Joint Variable Theta in Radian

        T1= (T1/180.0)*np.pi
        T2 = (T2/180.0)*np.pi   



        # Rows = no. of HTM, Colums  = no. of Parameter
        # THETA ALPHA  r d
        DHPT = [[T1, (90.0/180.0)*np.pi, 0, a1],
               [T2+(90.0/180.0)*np.pi, (90.0/180.0)*np.pi, a2, 0],
               [(0.0/180.0)*np.pi, (0.0/180.0)*np.pi,0, a3+d3]]


        i = 0
        H0_1 = [[np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -
                np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
                [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
                [0, 0, 0, 1]]


        i = 1
        H1_2 = [[np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -
                np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
                [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
                [0, 0, 0, 1]]

        i = 2
        H2_3 = [[np.cos(DHPT[i][0]), -np.sin(DHPT[i][0])*np.cos(DHPT[i][1]), np.sin(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]), np.cos(DHPT[i][0])*np.cos(DHPT[i][1]), -
                np.cos(DHPT[i][0])*np.sin(DHPT[i][1]), DHPT[i][2]*np.sin(DHPT[i][0])],
                [0, np.sin(DHPT[i][1]), np.cos(DHPT[i][1]), DHPT[i][3]],
                [0, 0, 0, 1]]



        # Position Joint
        H0_1 = np.matrix(H0_1)

        H0_2 = np.dot(H0_1, H1_2)
        H0_3 = np.dot(H0_2, H2_3)
        
        H0_2 = np.matrix(H0_2)
        print("H0_3 = ")
        print(np.matrix(np.around(H0_3,3)))

        X0_3 = H0_3[0,3]
        X = window['X'].Update(np.around(X0_3,3))

        Y0_3 = H0_3[1,3]
        Y = window['Y'].Update(np.around(Y0_3,3))
        Z0_3 = H0_3[2,3]
        Z = window['Z'].Update(np.around(Z0_3,3))

        disable_J.update(disabled = False)
        disable_Fk.update(disabled =True)


    elif event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')

    elif event == 'Jacobian Matrix(J)':

        Z_1 = [[0],[0],[1]] #the 0 0 1 vector

        # row 1 to 3 columm 1
        J1a = [[1,0,0], [0,1,0],[0,0,1]]
        J1a = np.dot(J1a,Z_1)

        
        J1b_1 = H0_3[0:3,3:]
        J1b_1 = np.matrix(J1b_1)

        J1b_2 = [[0],[0],[0]]

        J1b=J1b_1-J1b_2


        J1 = [[(J1a[1,0]*J1b[2,0])-(J1a[2,0]*J1b[1,0])],
            [(J1a[2,0]*J1b[0,0])-(J1a[0,0]*J1b[2,0])],
            [(J1a[0,0]*J1b[1,0])-(J1a[1,0]*J1b[0,0])]]

        
        #row 1 to 3 columm 2
       


        J2a = H0_1[0:3,0:3]
        J2a = np.dot(J2a,Z_1)
        

        J2b_1 = H0_3[0:3,3:]
        J2b_1 = np.matrix(J2b_1)
        

        J2b_2 = H0_1[0:3,3:]
        J2b_2 = np.matrix(J2b_2)
        

        J2b=J2b_1-J2b_2
            

        J2 = [[(J2a[1,0]*J2b[2,0])-(J2a[2,0]*J2b[1,0])],
            [(J2a[2,0]*J2b[0,0])-(J2a[0,0]*J2b[2,0])],
            [(J2a[0,0]*J2b[1,0])-(J2a[1,0]*J2b[0,0])]]

        #row 1 to 3 columm 3
        J3 = H0_2[0:3,0:3]
        J3 = np.dot(J3,Z_1)
        J3 = np.matrix(J3)
        
        J4= [[1,0,0], [0,1,0],[0,0,1]]
        J4 = np.dot(J4,Z_1)
        J4 = np.matrix(J4)
        

        J5 = H0_1[0:3,0:3]
        J5 = np.dot(J5,Z_1)
        

        J6 = [[0],[0],[0]]
        J6 = np.matrix(J6)
        
        JM1 =np.concatenate((J1,J2,J3),1)
        
        JM2 = np.concatenate((J4,J5,J6),1)
       

        J =np.concatenate( (JM1, JM2),0)
        sg.popup('J = ',np.around(J,3))

        disable_J.update(disabled =True)
        disable_DetJ.update(disabled =False)
        disable_IJ.update(disabled =False)
        disable_TJ.update(disabled =False)

    elif event == 'Det(J)':

        DJ = np.linalg.det(JM1)
        #print("DJ = ", DJ)
        
        sg.popup('DJ = ',np.around (DJ,3))
        disable_DetJ.update(disabled =True)

        if 0.0 >= DJ > -1.0:
          disable_IJ.update(disabled =True)
          sg.popup('Warning: Jacobian Matrix is Non-invertable!')

        elif DJ != 0.0 or DJ != -0 :
            disable_IJ.update(disabled =False)
            
    elif event == 'Inverse of J':
        #Inv(J)
        IJ =np.linalg.inv(JM1)
        sg.popup('IJ = ', np.around (IJ,3))
        disable_IJ.update(disabled =True)

    elif event == 'Transpose of J':
        TJ = np.transpose(JM1)
        sg.popup('TJ = ', np.around (TJ,3))
        disable_TJ.update(disabled =True)

    elif event == 'Solve Inverse Kinematics':
        sg.popup("Warning!! Disable Forward Kinematics and Jacobian Matrix!")
        Inverse_Kinematics_window()
        
window.close()