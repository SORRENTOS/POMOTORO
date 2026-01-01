import flet as ft

def handle_dismissal(e):
        print(f"Drawer dismissed!")

def handle_change(e):
        print(f"Selected Index changed: {e.control.selected_index}")
        page.close(drawer)


def GenerarDrawer():
    drawerView = ft.NavigationDrawer(
            on_dismiss=handle_dismissal,
            on_change=handle_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=ft.Icons.PHONE,
                ),
            ],
        )
    return drawerView