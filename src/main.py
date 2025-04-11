import flet as ft


def main(page: ft.Page):
    page.title = "Таксі лабіринт"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.WHITE)
    page.bgcolor = "#0bb817"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.fonts = {
        "Tektur": "fonts/Tektur-Medium.ttf",
        "Tektur-Bold": "fonts/Tektur-Bold.ttf"
    }

    Header_bar = ft.AppBar(
        leading=ft.Icon(ft.Icons.LOCAL_TAXI),
        leading_width=40,
        title=ft.Text("ТАКСІ\nЛАБІРИНТ",
                      text_align="center",
                      font_family="Tektur",
                      color=ft.Colors.WHITE),
        center_title=False,
        bgcolor="#0bb817",
        actions=[
            ft.Container(
                content=ft.Text(
                    "23156489",
                    size=20,
                    color=ft.Colors.WHITE,
                    selectable=True,
                ),
                padding=ft.padding.only(left=10, top=5, right=10, bottom=5),
                margin=ft.margin.only(left=10, top=5, right=20, bottom=5),
                border_radius=30,
                border=ft.border.all(3, ft.Colors.WHITE),
            )
        ],
    )

    slogan = ft.Text(
        value="Зручно, комфортно, завжди вчасно.\nТаксі Лабіринт - завжди поруч",
        size=45,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )
    call_us = ft.Text(
        value="Звоніть для замовлення [23156489]\n або завантажте наш додаток",
        size=30,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    BGimage = ft.Image("images/bgCar.jpg", width=page.width, height=page.height)

    app_links = ft.Row(
        controls=[
            ft.TextButton(
                content=ft.Image("images/GooglePlay.png"),
                on_click=lambda e: page.launch_url("https://apps.apple.com"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    overlay_color=ft.colors.TRANSPARENT,
                ),
            ),
            ft.TextButton(
                content=ft.Image("images/AppStore.png"),
                on_click=lambda e: page.launch_url("https://play.google.com"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    overlay_color=ft.colors.TRANSPARENT,
                ),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
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
        alignment=ft.alignment.center
    )

    main_container = ft.Container(content=ft.Column(
        controls=[
            slogan_container,
            app_links,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=True,
        height=page.height,
        width=page.width,
        blur=ft.Blur(sigma_x=10, sigma_y=10),
    )

    gradient = ft.Container(
        width=page.width,
        height=page.height,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[Header_bar.bgcolor, "#AAFEB0"],
        )
    )
    stack = ft.Stack([gradient, BGimage, main_container], expand=True)

    page.add(stack)

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
