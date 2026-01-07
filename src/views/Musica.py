import flet as ft




class contendedorMusica(ft.Container):
    def __init__(self):
        super().__init__()
        self.contenederMusica = ft.Container(image= ft.DecorationImage(src="images/jazz.jpg",fit=ft.ImageFit.COVER),
        width=150
        ,height=150
        ,border_radius=10,
        margin=ft.margin.only(left=15)
        )

        self.tituloMusica = ft.Container(content=ft.Text("Jazz para estudiar",color=ft.Colors.WHITE),width=150,height=150,margin=ft.margin.only(left=15),alignment=ft.alignment.bottom_center,padding=10)
        self.btnMusica =ft.Container(content=ft.IconButton(icon=ft.Icons.PLAY_ARROW_ROUNDED,width=150,height=150,icon_size=70,padding=0),width=150,height=150,margin=ft.margin.only(left=15),alignment=ft.alignment.center)

        self.stackMusica = ft.Stack([
            self.contenederMusica,
            self.tituloMusica,
            self.btnMusica

        ])
        self.content = self.stackMusica


class contendedorInicio(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.height = 350
        self.width = 500
        self.alignment = ft.alignment.top_center
        self.bgcolor ="#c1121f"


        self.columnaMusica= ft.Column([
            contendedorMusica()

        ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.START,width=500)
        self.content = self.columnaMusica
    




def musica_view (drawerMenu,navBar):

    PerfilView  = ft.View(
    "/perfil",[
    contendedorInicio()

        

    ],vertical_alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment= ft.CrossAxisAlignment.CENTER)


    PerfilView.drawer = drawerMenu
    PerfilView.navigation_bar = navBar
    PerfilView.bgcolor = "#fdf0d5"


    return PerfilView    
