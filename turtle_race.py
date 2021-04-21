from turtle import *
import time
import random

def start_finish_line():
    start_line = Turtle()
    start_line.pensize(3)
    start_line.pencolor("red")
    start_line.up()
    start_line.setpos(-300, 200)
    start_line.down()
    start_line.setpos(-300, -200)
    start_line.hideturtle()

    global finish_line
    finish_line = Turtle()
    finish_line.pensize(3)
    finish_line.pencolor("blue")
    finish_line.up()
    finish_line.setpos(300, 200)
    finish_line.down()
    finish_line.setpos(300, -200)
    finish_line.hideturtle()

def title_screen(race_track):
    wn = Screen()
    wn.title("Welcome to Turtle Race!")
    if race_track == 1:
        wn.bgpic("race_tracks\green_valley.gif")
    elif race_track == 2:
        wn.bgpic("race_tracks\haunted_race.gif")
    elif race_track == 3:
        wn.bgpic("race_tracks\\farm_race.gif")
    elif race_track == 4:
        wn.bgpic("race_tracks\\2dBeach.gif")
    elif race_track == 5:
        wn.bgpic("race_tracks\castle.gif")
    else:
        wn.bgpic("race_tracks\lake_town.gif")

def turtles(color, y_pos):
    player = Turtle()
    player.up()
    player.color(color)
    player.setpos(-320, y_pos)
    player.shape("turtle")

    return player

def turtle_speed(spd):
    speed = 1.0
    possible_speed = []
    for i in range(1,33):
        possible_speed.append(speed)
        speed += 0.1
    return possible_speed[spd]

def player_speed():
    turtle_spd = turtle_speed(random.randint(0,31))

    return turtle_spd    

def winner_message(player_num):
    global winner
    winner = Turtle()
    winner.up()
    winner.hideturtle()
    winner.setpos(0,250)
    winner.color('black')
    winner.write(player_num, move=False, align="center", font=("Arial", 42, "normal"))

def player_standings(standings):
    y_pos = 170
    global placement
    placement = Turtle()
    placement.ht()
    placement.penup()
    
    for i in range(2, len(standings)+1):
        placement.setpos(-95, y_pos)
        if i == 2:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}nd place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 3:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}rd place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 4:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 5:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 6:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 7:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
                
        elif i == 8:
            if standings[i-1] == player1.xcor():
                placement.write(f"Player 1 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player2.xcor():
                placement.write(f"Player 2 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player3.xcor():
                placement.write(f"Player 3 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player4.xcor():
                placement.write(f"Player 4 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player5.xcor():
                placement.write(f"Player 5 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player6.xcor():
                placement.write(f"Player 6 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player7.xcor():
                placement.write(f"Player 7 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            elif standings[i-1] == player8.xcor():
                placement.write(f"Player 8 came in {i}th place!", move=False, align="center", font=("Arial", 25, "normal"))
            
        y_pos -= 63
    
def timer():
    timer = 3
    count_down = Turtle()
    count_down.up()
    count_down.hideturtle()
    count_down.setpos(0, 250)
    
    for i in range(1,4):
        count_down.write(str(timer), move=False, align="center", font=("Arial", 56, "normal"))    
        time.sleep(1)
        count_down.clear()
        if timer == 1:
            count_down.write("GO!", move=False, align="center", font=("Arial", 56, "normal"))
            time.sleep(1)
            count_down.clear()
            count_down.write("", move=False, align="center", font=("Arial", 56, "normal"))
             
        timer -= 1

exit_game = ''
total_win_count = [0, 0, 0, 0, 0, 0, 0, 0]
while exit_game.lower() != 'quit' and exit_game.lower() != 'q':
    possible_tracks = '''Enter 1 to play Green Valley.     Enter 2 to play Haunted Graveyard.
    Enter 3 to play Farm.                  Enter 4 to play the Beach
    Enter 5 to play Castle                 Enter 6 to play Lake Town'''
    track_choice = numinput("Choose your track", possible_tracks, 1, minval=1, maxval=6)
    title_screen(track_choice)

    num_players_title = "how many people are playing?"
    num_players_prompt = "you can choose between 2 and 8 players"
    num_players = numinput(num_players_title.title(), num_players_prompt.title(), 2, minval=2, maxval=8)

    colors = []
    color_choice = ['red', 'blue', 'green', 'yellow', 'pink', 'purple', 'orange', 'black']
    color_options = '''Please choose one of the following colors:
red, blue, green, yellow
pink, purple, orange, or black'''
    for i in range(1, int(num_players)+1):
        player_color = textinput("player " + str(i), color_options.title())
        if player_color.lower() not in color_choice:
            player_color = textinput("player " + str(i), color_options.title())
        colors.append(player_color)

    #creates that start and finish line for the race    
    start_finish_line()

    #Assigns a color to each player
    player1 = turtles(colors[0], 25)
    player2 = turtles(colors[1], -25)
    if num_players > 2:
        player3 = turtles(colors[2], 75)   
    if num_players > 3:
        player4 = turtles(colors[3], -75)  
    if num_players > 4:
        player5 = turtles(colors[4], 125)  
    if num_players > 5:
        player6 = turtles(colors[5], -125)   
    if num_players > 6:
        player7 = turtles(colors[6], 175)
    if num_players > 7:
        player8 = turtles(colors[7], -175)
        
    # function to creater the timer before start of race
    timer()

    winner = Turtle()
    winner.hideturtle()

    player_wins = Turtle()
    player_wins.ht()

    while True:
        # loop to determine a winner and add to their win count
        player1.forward(player_speed())
        if player1.xcor() >= finish_line.xcor():
            total_win_count[0] += 1
            winner_message("player 1 is the winner!".title())
            break
        player2.forward(player_speed())
        if player2.xcor() >= finish_line.xcor():
            total_win_count[1] += 1
            winner_message("player 2 is the winner!".title())
            break
        if num_players > 2:
            player3.forward(player_speed())
            if player3.xcor() >= finish_line.xcor():
                total_win_count[2] += 1
                winner_message("player 3 is the winner!".title())
                break
        if num_players > 3:
            player4.forward(player_speed())
            if player4.xcor() >= finish_line.xcor():
                total_win_count[3] += 1
                winner_message("player 4 is the winner!".title())
                break
        if num_players > 4:
            player5.forward(player_speed())
            if player5.xcor() >= finish_line.xcor():
                total_win_count[4] += 1
                winner_message("player 5 is the winner!".title())
                break
        if num_players > 5:
            player6.forward(player_speed())
            if player6.xcor() >= finish_line.xcor():
                total_win_count[5] += 1
                winner_message("player 6 is the winner!".title())
                break
        if num_players > 6:
            player7.forward(player_speed())
            if player7.xcor() >= finish_line.xcor():
                total_win_count[6] += 1
                winner_message("player 7 is the winner!".title())
                break
        if num_players > 7:
            player8.forward(player_speed())
            if player8.xcor() >= finish_line.xcor():
                total_win_count[7] += 1
                winner_message("player 8 is the winner!".title())
                break
            
        player_speed()
            
    player1.write(round(player1.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    player2.write(round(player2.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 2:
        player3.write(round(player3.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 3:
        player4.write(round(player4.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 4:
        player5.write(round(player5.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 5:
        player6.write(round(player6.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 6:
        player7.write(round(player7.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))
    if num_players > 7:
        player8.write(round(player8.xcor(), 2), move=True, align="center", font=("Arial", 16, "normal"))

    standings = []

    standings.append(player1.xcor())
    standings.append(player2.xcor())
    if num_players > 2:
        standings.append(player3.xcor())
    if num_players > 3:
        standings.append(player4.xcor())
    if num_players > 4:
        standings.append(player5.xcor())
    if num_players > 5:
        standings.append(player6.xcor())
    if num_players > 6:
        standings.append(player7.xcor())
    if num_players > 7:
        standings.append(player8.xcor())
        
    standings.sort()
    standings.reverse()
    # function that prints out which placements of each player at the end of the race
    player_standings(standings)

    wins_pos = -600
    player_wins.penup()
    player_wins.setpos(wins_pos, 350)


    # Prints out how many wins each player has earned at the top of the screen
    player_wins.write("Total Wins By Each Player:", move=False, align="center", font=("Arial", 16, "normal"))
    wins_pos += 200
    player_wins.setpos(wins_pos, 350)

    for i in range(0,8):
        player_wins.write(f"Player {i+1}: {total_win_count[i]}", move=False, align="center", font=("Arial", 16, "normal"))
        wins_pos += 150
        player_wins.setpos(wins_pos, 350)

    exit_game = textinput("Would you like to play again?", "Enter quit or q to exit game. Enter any key to continue playing")
    player_wins.clear()
    placement.clear()
    winner.clear()
    player1.clear()
    player1.ht()
    player2.clear()
    player2.ht()
    if num_players > 2:
        player3.clear()
        player3.ht()
    if num_players > 3:
        player4.clear()
        player4.ht()
    if num_players > 4:
        player5.clear()
        player5.ht()
    if num_players > 5:
        player6.clear()
        player6.ht()
    if num_players > 6:
        player7.clear()
        player7.ht()
    if num_players > 7:
        player8.clear()
        player8.ht()
