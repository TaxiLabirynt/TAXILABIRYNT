import flet as ft


def main(page: ft.Page):
    page.title = "Таксі лабіринт"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.WHITE)
    page.bgcolor = ft.Colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
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
        bgcolor=ft.Colors.BLACK45,
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
        value="Замовляй вигідно, приїзджай вчасно",
        size=50,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )
    call_us = ft.Text(
        value="Звоніть для замовлення [23156489]\n або завнтажте наш додаток",
        size=30,
        color=ft.Colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    )

    left_image = ft.Image(
        src="images/bgLeft.png",
        fit=ft.ImageFit.FILL,
        width=200,
    )
    right_image = ft.Image(
        src="images/bgRight.png",
        fit=ft.ImageFit.FILL,
        width=200,
    )

    images_row = ft.Row(
        controls=[left_image, right_image],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

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

    main_container = ft.Container(content=ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [slogan, call_us],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.top_center,
            ),
            app_links,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ), )

    stack = ft.Stack([images_row, main_container], expand=True)

    page.add(ft.Column(
        [stack],
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    ))

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")
