import flet as ft
from views.home import homeView


def main(page: ft.Page):

    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route) #page.go("/ruta")


# FUNCIONES DEL LOGIN
    def login(e):
        page.go("/home")
   


    comlumnaLogin = ft.Column([

       ft.Container(content= ft.Text(value="correo"),alignment=ft.alignment.center),
        ft.TextField(label="tuCorreo@direccion.com",border_width=0,bgcolor="#780000"),
        ft.Text(value="contrasena",text_align=ft.TextAlign.CENTER),
        ft.TextField(password=True,border_width=0,bgcolor="#780000"),
        ft.CupertinoButton(bgcolor="#fdf0d5",text="iniciar sesion",border_radius=10,on_click=login,color=ft.Colors.BLACK)





    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER)



    containerLoign = ft.Container(content=comlumnaLogin, 
                    bgcolor="#c1121f"
    ,width=300,height=400,
    border_radius=10,
    border= ft.border.all(0,"#c1121f"),
    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color ="#c1121f",
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.NORMAL,
        
    ),padding= ft.padding.all(20)
    )

    containerMaster = ft.Container(content=containerLoign,alignment=ft.alignment.center,expand=True)
    

    def route_change(route):
        page.views.clear()
        page.views.append(
            #AQUI VAN LAS VIEWS
            #ft.view("/",[controladores])


            ft.View("/",[containerMaster],bgcolor="#fdf0d5"),
        )
        if page.route == "/home":
            page.views.append(homeView)
        page.update()




    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)



