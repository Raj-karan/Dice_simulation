import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

# Window
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Dice Silmuation")

all_dice_width = 50

# positions
poses = [25,125,225,325,425,525]
plus_chance = [50, 50, 50, 50, 50, 50]

# some variables
winner_anounced = False
start = False
running = True
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
WINNERFONT = pygame.font.Font('freesansbold.ttf', 30)
SPEEDFONT = pygame.font.Font('freesansbold.ttf', 15)
clicked = False
dice_speed = 4

# positions of speed buttons
slow_pos_x, slow_pos_y = 110, 3

medium_pos_x, medium_pos_y = 150, 3

fast_pos_x, fast_pos_y = 190, 3

while running:
	clock.tick(60)
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				clicked = True
		if event.type == pygame.MOUSEBUTTONUP:
				clicked = False

	# race logic
	if start:
		if not winner_anounced:
			chance = random.choice([x for x in range(6)])
			plus_chance[chance] += dice_speed
		for x in plus_chance:
			if x >= 550:
				winner_anounced = True

	# all rect
	one_rect = pygame.Rect(poses[0], plus_chance[0], all_dice_width, all_dice_width)
	two_rect = pygame.Rect(poses[1], plus_chance[1], all_dice_width, all_dice_width)
	three_rect = pygame.Rect(poses[2], plus_chance[2], all_dice_width, all_dice_width)
	four_rect = pygame.Rect(poses[3], plus_chance[3], all_dice_width, all_dice_width)
	five_rect = pygame.Rect(poses[4], plus_chance[4], all_dice_width, all_dice_width)
	six_rect = pygame.Rect(poses[5], plus_chance[5], all_dice_width, all_dice_width)

	# ALL Numbers 
	one   = BASICFONT.render("1", True, (0, 0, 0))
	one_pos = (poses[0]+18, plus_chance[0]+15)

	two   = BASICFONT.render("2", True, (0, 0, 0))
	two_pos = (poses[1]+18, plus_chance[1]+15)

	three = BASICFONT.render("3", True, (0, 0, 0))
	three_pos = (poses[2]+18, plus_chance[2]+15)

	four  = BASICFONT.render("4", True, (0, 0, 0))
	four_pos = (poses[3]+18, plus_chance[3]+15)

	five  = BASICFONT.render("5", True, (0, 0, 0))
	five_pos = (poses[4]+18, plus_chance[4]+15)

	six   = BASICFONT.render("6", True, (0, 0, 0))
	six_pos = (poses[5]+18, plus_chance[5]+15)

	# Winner Text
	winner_font = WINNERFONT.render("Winner", True, (255, 255, 255))
	winner_pos  = (250, 560)

	# speed of Dice maniplulation
	speed_font = BASICFONT.render("Dice speed:", True, (255, 255, 255))
	speed_pos  = (2, 10)

	slow_rect = pygame.Rect(slow_pos_x, slow_pos_y, 30, 30)
	pygame.draw.rect(screen, (255, 255, 255), slow_rect, 2)

	medium_rect = pygame.Rect(medium_pos_x, medium_pos_y, 30, 30)
	pygame.draw.rect(screen, (255, 255, 255), medium_rect, 2)

	fast_rect = pygame.Rect(fast_pos_x, fast_pos_y, 30, 30)
	pygame.draw.rect(screen, (255, 255, 255), fast_rect, 2)

	slow_speed = SPEEDFONT.render("4", True, (255, 255, 255))
	slow_speed_pos = (slow_pos_x+10, slow_pos_y+8)

	medium_speed = SPEEDFONT.render("8", True, (255, 255, 255))
	medium_speed_pos = (medium_pos_x+10, medium_pos_y+8)

	fast_speed = SPEEDFONT.render("12", True, (255, 255, 255))
	fast_speed_pos = (fast_pos_x+5, fast_pos_y+8)

	# Drawing on screen
	pygame.draw.rect(screen, (255, 255, 255), one_rect)
	pygame.draw.rect(screen, (255, 255, 255), two_rect)
	pygame.draw.rect(screen, (255, 255, 255), three_rect)
	pygame.draw.rect(screen, (255, 255, 255), four_rect)
	pygame.draw.rect(screen, (255, 255, 255), five_rect)
	pygame.draw.rect(screen, (255, 255, 255), six_rect)
	pygame.draw.line(screen, (255, 255, 255), (0,550), (600, 550), 6)

	screen.blit(winner_font, winner_pos)
	screen.blit(one, one_pos)
	screen.blit(two, two_pos)
	screen.blit(three, three_pos)
	screen.blit(four, four_pos)
	screen.blit(five, five_pos)
	screen.blit(six, six_pos)
	screen.blit(speed_font, speed_pos)
	screen.blit(slow_speed, slow_speed_pos)
	screen.blit(medium_speed, medium_speed_pos)
	screen.blit(fast_speed, fast_speed_pos)


	# button start and reset
	start_rect_frame = pygame.Rect(310, 3, 60, 30)
	pygame.draw.rect(screen, (255, 255, 255), start_rect_frame, 2)

	reset_rect_frame = pygame.Rect(250, 3, 60, 30)
	pygame.draw.rect(screen, (255, 255, 255), reset_rect_frame, 2)

	start_font = BASICFONT.render("Start", True, (255, 255, 255))
	start_rect = (320, 10)
	reset_font = BASICFONT.render("Reset", True, (255, 255, 255))
	reset_rect = (255, 10)

	screen.blit(start_font, start_rect)
	screen.blit(reset_font, reset_rect)

	# Check for button press
	mx, my = pygame.mouse.get_pos()
	if start_rect_frame.collidepoint(mx, my):
		if clicked:
			start = True
	if reset_rect_frame.collidepoint(mx, my):
		if clicked:
			start = False
			for x in range(len(plus_chance)):
				plus_chance[x] = 50
			winner_anounced = False

	if slow_rect.collidepoint(mx, my):
		if clicked:
			dice_speed = 4
	elif medium_rect.collidepoint(mx, my):
		if clicked:
			dice_speed = 8
	elif fast_rect.collidepoint(mx, my):
		if clicked:
			dice_speed = 12

	pygame.display.update()