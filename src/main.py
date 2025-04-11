import flet as ft

mainColor = "#4D308F"

def main(page: ft.Page):
    page.title = "Таксі Лабіринт — зручно, комфортно, завжди вчасно"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.WHITE)
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.fonts = {
        "Tektur": "fonts/Tektur-Medium.ttf",
        "Tektur-Bold": "fonts/Tektur-Bold.ttf"
    }

    Header_bar = ft.AppBar(
        title=ft.Text("ТАКСІ ЛАБІРИНТ 542",
                      text_align="center",
                      font_family="Tektur",
                      color=ft.Colors.BLACK),
        center_title=True,
        bgcolor="#F1C104",
    )

    slogan = ft.Text(
        value="Зручно, комфортно, завжди вчасно.\nТаксі Лабіринт - завжди поруч",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )
    call_us = ft.Text(
        value="Замовляйте за номером [23156489]\n або завантажте наш додаток",
        size=15,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    app_links = ft.Row(
        controls=[
            ft.TextButton(
                content=ft.Image("images/GooglePlay.png"),
                on_click=lambda e: page.launch_url("https://play.google.com"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    overlay_color=ft.colors.TRANSPARENT,
                ),
            ),
            ft.TextButton(
                content=ft.Image("images/AppStore.png"),
                on_click=lambda e: page.launch_url("https://apps.apple.com"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    overlay_color=ft.colors.TRANSPARENT,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )
    app_links_col = ft.Column(
        [ft.Text("Не зволікай та замовляй Таксі Лабіринт!", size=15, color=ft.Colors.BLACK, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD), app_links],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    app_links_container = ft.Container(
        content=app_links_col,
        padding=ft.padding.only(bottom=20)
    )
    page.appbar = Header_bar

    slogan_content = ft.Column(
        [slogan, call_us],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    slogan_container = ft.Container(
        content=slogan_content,
        padding=20,
        border_radius=10,
        alignment=ft.alignment.center,
        expand=True
    )

    content_column = ft.Column(
        [
            slogan_container,
            app_links_container,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.END,
        spacing=0,
    )
    
    content_column_container = ft.Container(
        content=content_column,
        margin=ft.margin.only(top=0)
    )

    main_container = ft.Container(
        content=content_column_container,
        alignment=ft.alignment.center,
        width=page.width,
        height=page.height*0.8
    )

    background_image = ft.Image(
        src="images/BGLayer1.png",
        fit=ft.ImageFit.COVER,
        expand=True,
    )

    main_container_with_bg = ft.Stack(
        [
            background_image,
            main_container
        ],
        expand=True,
        alignment=ft.alignment.center
    )

    page.add(main_container_with_bg)

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
