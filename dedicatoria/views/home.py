from flet import *
import math

def home_page(page: Page):
    return View(
        route="/home",
        controls=[
            Container(
                Column([
                    
                ], horizontal_alignment=CrossAxisAlignment.CENTER),
                alignment=alignment.center,
                gradient=LinearGradient(
                    begin=alignment.top_left,
                    end=alignment.bottom_right,
                    colors=[
                        "#0b0b44",
                        "#0919a1"  
                    ],
                    tile_mode=GradientTileMode.MIRROR,
                    rotation=math.pi / 3,
                ),
                width=page.window.width,
                height=page.window.height,
                border_radius=1,
        )
        ], scroll=ScrollMode.HIDDEN
    )