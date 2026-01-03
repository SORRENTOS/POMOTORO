import flet as ft
import asyncio

#CREACION CLASE DE TIMER

class Timer(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor ="#c1121f"
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.texto = ft.Text(value=f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}",size=50,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        self.contenedorTexto = ft.Container(content=self.texto,bgcolor="#780000",padding=10,border_radius=10,margin= ft.margin.only(top=15))
        
        self.border_radius = 10
        self.height = 350
        self.width = 500
        self.alignment = ft.alignment.top_center
        #Botones para el tiempo
        




        self.InputMinutos = ft.TextField(label="0",bgcolor="#780000",border_width=0,border_radius=20,width=70,text_align=ft.TextAlign.CENTER)
        self.btnSumarMinuto = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_UP_ROUNDED,on_click= lambda x : self.modificar_minutos("+"),expand=True,bgcolor="#780000",icon_color="#fdf0d5")
        self.btnRestarMinuto = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN_ROUNDED,on_click = lambda x : self.modificar_minutos("-"),expand=True,bgcolor="#780000",icon_color="#fdf0d5")
        self.columnaMinutos = ft.Column([
            ft.Text("Minutos"),
            self.btnSumarMinuto,
            self.InputMinutos,

        

            self.btnRestarMinuto


        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER,width=100)

        self.InputHoras = ft.TextField(label="0",bgcolor="#780000",border_width=0,border_radius=20,width= 70)
        self.btnSumarHora = ft.IconButton(icon= ft.Icons.ARROW_CIRCLE_UP_ROUNDED,on_click= lambda x : self.modificar_horas("+"),expand=True,bgcolor="#780000",icon_color="#fdf0d5")
        self.btnRestarhora = ft.IconButton(icon=ft.Icons.ARROW_CIRCLE_DOWN_ROUNDED,on_click = lambda x : self.modificar_horas("-"),expand=True,bgcolor="#780000",icon_color="#fdf0d5")
        self.columnahora = ft.Column([
            ft.Text("Horas"),
            self.btnSumarHora,
            self.InputHoras,
            self.btnRestarhora


        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER,width=100)





        #controles
        controles = ft.Column([
            self.contenedorTexto,
            ft.Button(text="timer",bgcolor=ft.Colors.BLACK,on_click= self.timer),
            ft.Row([self.columnahora,self.columnaMinutos],alignment=ft.MainAxisAlignment.CENTER,wrap=True)


        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.START,expand=True)
        self.content = controles




    async def timer(self,e):
            i = 0
            #ira descontando tiempo!
            inicio = True
            while(self.horas >= 0 or inicio):
                #print("hora")
                while(self.minutos > 0) or inicio:
                    print("minuto")
                    if (self.minutos - 1) >= 0:
                        self.minutos -=1
                        self.segundos = 59
                    while(self.segundos>0 or inicio):
                       # print("segundo")
                        inicio = False
                        if (self.segundos - 1) >= 0:
                            self.segundos -= 1
                        self.texto.value = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
                        await asyncio.sleep(1)
                        self.update()

                    f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
                    self.update()                            
                if (self.horas - 1) >= 0:
                    self.horas -=1
                    self.minutos = 59
                self.update()                                 
   
    def modificar_minutos(self,x):
        if x == "+":
            self.minutos += 1
        elif x =="-":
            self.minutos -=1
        self.texto.value = f"{self.horas}:{self.minutos}:{self.segundos}"

        self.update()
    def modificar_horas(self,x):
        if x == "+":
            self.horas += 1
        elif x =="-":
            self.horas -=1
        self.texto.value = f"{self.horas}:{self.minutos}:{self.segundos}"

        self.update()


class Tarea(ft.Container):
    def __init__(self,contenido):
        super().__init__()
        self.bgcolor ="#c1121f"
        self.offset = ft.Offset(-2,0)
        self.animate_offset = ft.Animation(1000)
        self.text = ft.Text(value=str(contenido),style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH))
        self.checkBtn = ft.Checkbox()
        self.content = ft.Row([self.text,self.checkBtn],alignment=ft.MainAxisAlignment.CENTER)
    def animateTarea(self):
        self.offset = ft.Offset(0, 0)
        self.update()

class TodoList(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor ="#c1121f"

        self.InputTarea = ft.TextField(border_width=0,border_radius=10,bgcolor="#780000",label="Cosas por hacer...")
        self.btnAgregarTarea = ft.IconButton(icon=ft.Icons.ADD,bgcolor="#780000",on_click=self.agregarTarera,icon_color="#fdf0d5")
        self.alignment = ft.alignment.center
        self.border_radius = 10
        self.height = 300
        self.width = 500
        self.padding = 10


        self.filaTarea = ft.Row([self.InputTarea,self.btnAgregarTarea],alignment=ft.MainAxisAlignment.CENTER)




        self.columnaDeTareas = ft.Column([],horizontal_alignment=ft.CrossAxisAlignment.CENTER,scroll=ft.ScrollMode.AUTO,expand=True)
        self.content = ft.Column([self.filaTarea,self.columnaDeTareas])



    
    def agregarTarera(self,e):
            nuevatarea = Tarea(self.InputTarea.value)
            self.columnaDeTareas.controls.append(nuevatarea)
            self.update()
            self.page.run_task(self.anim_wait, nuevatarea)
            #self.update()
    async def anim_wait(self,tarea):
        await asyncio.sleep(0.01)
        tarea.animateTarea()



def home_view (drawerMenu,navBar):

    homeView  = ft.View(
    "/home",[
        Timer(),
        TodoList(),


        

    ],vertical_alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment= ft.CrossAxisAlignment.CENTER





    )
    homeView.drawer =drawerMenu
    homeView.navigation_bar = navBar
    homeView.bgcolor = "#fdf0d5"
    return homeView