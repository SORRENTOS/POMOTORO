import flet as ft
import asyncio

#CREACION CLASE DE TIMER

class Timer(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor ="#c1121f"
        self.segundos = 0
        self.minutos = 1
        self.horas = 0
        self.texto = ft.Text(value=f"{self.horas}:{self.minutos}:{self.segundos}",color=ft.Colors.BLACK)



        #Botones para el tiempo
        




        self.InputMinutos = ft.TextField(label="0")
        self.btnSumarMinuto = ft.IconButton(icon=ft.Icons.PLUS_ONE,on_click= lambda x : self.modificar_minutos("+"))
        self.btnRestarMinuto = ft.IconButton(icon=ft.Icons.PLUS_ONE,on_click = lambda x : self.modificar_minutos("-"))
        self.columnaMinutos = ft.Column([
            self.btnSumarMinuto,
            self.InputMinutos,
            self.btnRestarMinuto


        ])




        #controles
        controles = ft.ResponsiveRow([

            self.texto,
            ft.Button(text="timer",bgcolor=ft.Colors.BLACK,on_click= self.timer),
            self.columnaMinutos

        ])
        self.content = controles




    async def timer(self,e):
            i = 0
            #ira descontando tiempo!
            inicio = True
            while(self.horas >= 0 or inicio):
                print("hora")
                while(self.minutos > 0) or inicio:
                    print("minuto")
                    if (self.minutos - 1) >= 0:
                        self.minutos -=1
                        self.segundos = 59
                    while(self.segundos>0 or inicio):
                        print("segundo")
                        inicio = False
                        if (self.segundos - 1) >= 0:
                            self.segundos -= 1
                        self.texto.value = f"{self.horas}:{self.minutos}:{self.segundos}"
                        await asyncio.sleep(1)
                        self.update()

                    f"{self.horas}:{self.minutos}:{self.segundos}"
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
homeView  = ft.View(
"/home",[
    Timer(),
    ft.Text("hola chat")


    

]







)