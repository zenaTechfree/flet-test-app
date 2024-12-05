import flet as ft

def main(page: ft.Page):
    page.title = "Counter App"
    
    # 카운터 상태
    counter = ft.Text("0", size=40)
    
    def add_click(e):
        counter.value = str(int(counter.value) + 1)
        page.update()
    
    # UI 구성
    page.add(
        ft.Column(
            controls=[
                counter,
                ft.ElevatedButton("+1", on_click=add_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)