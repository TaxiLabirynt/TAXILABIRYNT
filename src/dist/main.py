import flet as ft
import constants as const


def main(page: ft.Page):
    page.title = const.SITE_NAME
    page.theme = ft.Theme(color_scheme_seed=const.BG_COLOR)
    page.bgcolor = const.BG_COLOR
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        "Tektur": "fonts/Tektur-Medium.ttf",
        "Tektur-Bold": "fonts/Tektur-Bold.ttf"
    }

    Header_bar = ft.AppBar(
        leading=ft.Icon(const.TAXI_ICON),
        leading_width=40,
        title=ft.Text(const.SITE_HEADER_NAME.upper(),
                      text_align="center",
                      font_family="Tektur",
                      color=const.BG_COLOR),
        center_title=False,
        bgcolor=ft.Colors.BLACK45,
        actions=[
            ft.Container(
                content=ft.Text(
                    const.TAXI_NUMBER,
                    size=20,
                    color=const.BG_COLOR,
                    selectable=True,
                ),
                padding=ft.padding.only(left=10, top=5, right=10, bottom=5),
                margin=ft.margin.only(left=10, top=5, right=20, bottom=5),
                border_radius=30,
                border=ft.border.all(3, const.BG_COLOR),
            )
        ],
    )

    slogan = ft.Text(
        value=const.SLOGAN,
        size=50,
        color=const.MAIN_COLOR,
        text_align=ft.TextAlign.CENTER,
    )
    call_us = ft.Text(
        value=const.CALL_US,
        size=30,
        color=const.MAIN_COLOR,
        text_align=ft.TextAlign.CENTER,
    )

    left_image = ft.Image(
        src=const.BG_LEFT_IMAGE,
        fit=ft.ImageFit.FILL,
        width=200,
    )
    right_image = ft.Image(
        src=const.BG_RIGHT_IMAGE,
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
                content=ft.Image(const.PLAY_STORE),
                on_click=lambda e: page.launch_url(const.PLAY_STORE_LINK),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    overlay_color=ft.colors.TRANSPARENT,
                ),
            ),
            ft.TextButton(
                content=ft.Image(const.APP_STORE),
                on_click=lambda e: page.launch_url(const.APP_STORE_LINK),
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
