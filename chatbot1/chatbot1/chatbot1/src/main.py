import flet as ft

def main(page: ft.Page):
    page.title = "Chat con IA - PARTE 1"
    page.bgcolor = ft.Colors.BLUE_900
    
    mensajes = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
    prompt = ft.TextField(label="Escribe tu mensaje...", expand=True, multiline=True, min_lines=1, max_lines=4)
    
    def burbuja(texto, es_usuario):
        return ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        texto,
                        color=ft.Colors.BLUE_GREY_600 if es_usuario else ft.Colors.BLACK,
                        size=15,
                        selectable=True,
                    ),
                    bgcolor=ft.Colors.AMBER_ACCENT_200 if es_usuario else ft.Colors.GREY_300,
                    padding=12,
                    border_radius=30,
                    width=350,
                )
            ],
            alignment=ft.MainAxisAlignment.END if es_usuario else ft.MainAxisAlignment.START,
        )
    
    def enviar_click(e):
        texto = prompt.value.strip()
        if not texto:
            return
        mensajes.controls.append(burbuja(texto, es_usuario=True))
        prompt.value = ""
        page.update()
        mensajes.controls.append(burbuja("Hola, soy un bot simulado. ¡Parte 1 lista!", es_usuario=False))
        page.update()
        
    def limpiar_chat(e):
        mensajes.controls.clear()
        page.update()
        
    boton_enviar = ft.ElevatedButton("Enviar", on_click=enviar_click, bgcolor=ft.Colors.BROWN_200, color=ft.Colors.CYAN_ACCENT_200)
    prompt.on_sumbit = enviar_click
    
    page.add(
        ft.Column([
            ft.Row([ft.TextButton("Limpiar chat", on_click=limpiar_chat)], alignment=ft.MainAxisAlignment.START),
            mensajes,
            ft.Row([prompt, boton_enviar], vertical_alignment=ft.CrossAxisAlignment.END),
        ], expand=True)
    )
    
ft.app(target=main)