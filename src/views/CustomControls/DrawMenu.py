import flet as ft

def handle_dismissal(e):
        print(f"Drawer dismissed!")



def GenerarDrawer():
    drawerView = ft.NavigationDrawer(
            on_dismiss=handle_dismissal,
            bgcolor="#780000",
            controls=[
                ft.Container(height=12),

                ft.NavigationDrawerDestination(
                    label="Perfil",
                    icon=ft.Icons.PERSON,
                    selected_icon=ft.Icon(ft.Icons.PERSON),
                    
                ),

                ft.Container(height=12),
                ft.Divider(thickness=2),

                ft.NavigationDrawerDestination(
                    label="Estudiar",
                    icon=ft.Icons.AV_TIMER,
                    selected_icon=ft.Icon(ft.Icons.AV_TIMER),
                    
                ),
              
            ],
        )
    return drawerView