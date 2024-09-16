def example(page: ft.Page):
    size = 10
    gap = 3
    duration = 2000
    

    c1 = colors.PINK_500
    c2 = colors.AMBER_500
    c3 = colors.LIGHT_GREEN_500
    c4 = colors.DEEP_PURPLE_500
    c5 = colors.LIGHT_BLUE_500
    c6 = colors.RED_600
    
    all_colors = [
        colors.AMBER_400,
        colors.AMBER_ACCENT_400,
        colors.BLUE_400,
        colors.BROWN_400,
        colors.CYAN_700,
        colors.DEEP_ORANGE_500,
        colors.CYAN_500,
        colors.INDIGO_600,
        colors.ORANGE_ACCENT_100,
        colors.PINK,
        colors.RED_600,
        colors.GREEN_400,
        colors.GREEN_ACCENT_200,
        colors.TEAL_ACCENT_200,
        colors.LIGHT_BLUE_500,
    ]

    parts = [
        # K
        (0, 0, c1),
        (0, 1, c1),
        (0, 2, c1),
        (0, 3, c1),
        (0, 4, c1),
        (3, 0, c1),
        (2, 1, c1),
        (1, 2, c1),
        (1, 3, c1),
        (2, 3, c1),
        (3, 4, c1),
        # I
        (5, 0, c2),
        (5, 4, c2),
        (7, 0, c2),
        (7, 4, c2),
        (6, 0, c2),
        (6, 1, c2),
        (6, 2, c2),
        (6, 3, c2),
        (6, 4, c2),
        (6, 4, c2),
        (7, 4, c2),
        # N
        (9, 0, c3),
        (9, 1, c3),
        (9, 2, c3),
        (9, 3, c3),
        (9, 4, c3),
        (10, 0, c3),
        (10, 1, c3),
        (11, 2, c3),
        (12, 3, c3),
        (12, 4, c3),
        (13, 0, c3),
        (13, 1, c3),
        (13, 2, c3),
        (13, 3, c3),
        (13, 4, c3),
        # N
        (15, 0, c3),
        (15, 1, c3),
        (15, 2, c3),
        (15, 3, c3),
        (15, 4, c3),
        (16, 0, c3),
        (16, 1, c3),
        (17, 2, c3),
        (18, 3, c3),
        (18, 4, c3),
        (19, 0, c3),
        (19, 1, c3),
        (19, 2, c3),
        (19, 3, c3),
        (19, 4, c3),
        # E
        (21, 0, c4),
        (21, 1, c4),
        (21, 2, c4),
        (21, 3, c4),
        (21, 4, c4),
        (22, 0, c4),
        (22, 2, c4),
        (22, 4, c4),
        (23, 0, c4),
        (23, 2, c4),
        (23, 4, c4),
        # M
        (25, 0, c5),
        (25, 1, c5),
        (25, 2, c5),
        (25, 3, c5),
        (25, 4, c5),
        (26, 0, c5),
        (26, 1, c5),
        (27, 1, c5),
        (27, 2, c5),
        (28, 1, c5),
        (28, 0, c5),
        (29, 0, c5),
        (29, 1, c5),
        (29, 2, c5),
        (29, 3, c5),
        (29, 4, c5),
        # A
        (31, 0, c6),
        (31, 1, c6),
        (31, 2, c6),
        (31, 3, c6),
        (31, 4, c6),
        (32, 0, c6),
        (32, 2, c6),
        (33, 0, c6),
        (33, 2, c6),
        (34, 0, c6),
        (34, 1, c6),
        (34, 2, c6),
        (34, 3, c6),
        (34, 4, c6),
        
        
    ]

    width = 100 * (size + gap)
    # height = 5 * (size + gap)
    height = 30 * (size + gap)

    canvas = Stack(
        width=width,
        height=height,
        animate_scale=duration,
        animate_opacity=duration,
    )

    # spread parts randomly
    for i in range(len(parts)):
        canvas.controls.append(
            Container(
                animate=duration,
                animate_position=duration,
                animate_rotation=duration,
            )
        )

    def randomize(e):
        random.seed()
        for i in range(len(parts)):
            c = canvas.controls[i]
            part_size = random.randrange(int(size / 2), int(size * 3))
            c.left = random.randrange(0, width)
            c.top = random.randrange(0, height)
            c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        canvas.scale = 5
        canvas.opacity = 0.3
        go_button.visible = True
        page.update()

    def assemble(e):
        i = 0
        for left, top, bgcolor in parts:
            c = canvas.controls[i]
            c.left = left * (size + gap)
            c.top = top * (size + gap)
            c.bgcolor = bgcolor
            c.width = size
            c.height = size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        canvas.scale = 1
        canvas.opacity = 1
        go_button.visible = False
        page.update()

    go_button = ElevatedButton("Go!", on_click=assemble, visible=True)

    randomize(None)
    
    def delayed_assemble():
        assemble(None)

    timer = threading.Timer(0.3, delayed_assemble)
    timer.start()
    
    

    # return ft.Column(
    #     expand=True,
    #     alignment=ft.MainAxisAlignment.CENTER,
    #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    #     tight=True,
    #     controls=[
    #         canvas,
    #         go_button,
    #         again_button,
    #     ],
    # )

    
    
    return ft.Container(
        expand=True,
        padding=10,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
            controls=[
                canvas,
            ],
        ),
    )



    
    