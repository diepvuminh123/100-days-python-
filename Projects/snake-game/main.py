from mainsnake import Main
snake1 = Main()

snake1.setscreen(600, 600, "black")
snake1.setsnake("square", "white")
# Keep the window open until clicked
snake1.sc.exitonclick()
