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
                    label="Item 1",
                    icon=ft.Icons.Home,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                    
                ),
                ft.Divider(thickness=2),
              
            ],
        )
    return drawerView