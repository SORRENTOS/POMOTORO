import flet as ft





class contendedorPerfil(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.height = 350
        self.width = 500
        self.alignment = ft.alignment.top_center
        self.bgcolor ="#c1121f"





        self.columnaPerfil = ft.Column([
            ft.Icon(name=ft.Icons.PERSON,size= 50,color= "#fdf0d5")


        ],alignment=ft.MainAxisAlignment.CENTER)
        self.content = self.columnaPerfil
    




def perfil_view (drawerMenu,navBar):

    PerfilView  = ft.View(
    "/perfil",[
    contendedorPerfil()

        

    ],vertical_alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment= ft.CrossAxisAlignment.CENTER)


    PerfilView.drawer = drawerMenu
    PerfilView.navigation_bar = navBar
    PerfilView.bgcolor = "#fdf0d5"


    return PerfilView    
