import fresh_tomatoes
import media

'''
toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that come to life",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
		"A marine on an alien planet",
		"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
		"https://youtu.be/5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
'''

zootopia = media.Movie("Zootopia",
		"In a world populated by anthropomorphic mammals, "
		"a rabbit from rural Bunnyburrow named Judy Hopps "
		"fulfills her childhood dream of becoming the first "
		"rabbit police officer in Zootopia, an urban utopia.",
		"https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
		"https://youtu.be/bY73vFGhSVk")
#print(zootopia.title)
#print(zootopia.storyline)
#zootopia.show_trailer()

'''
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
		"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
		"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
		"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
		"https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
		"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
		"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "A really real reality show",
		"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
		"https://www.youtube.com/watch?v=4S9a5V9ODuY")
'''

up = media.Movie("Up", "Mr. Fredricksen and Russell goes on adventure",
		"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
		"https://www.youtube.com/watch?v=pkqzFUhGPJg")

finding_nemo = media.Movie("Finding Nemo", "Story about finding lost Nemo",
		"https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
		"https://www.youtube.com/watch?v=wZdpNglLbt8")

american_sniper = media.Movie("American Sniper", "Life of Chris Kyle",
		"https://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg",
		"https://www.youtube.com/watch?v=99k3u9ay1gs")

argo = media.Movie("Argo", "Rescuing American citizen",
		"https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg",
		"https://www.youtube.com/watch?v=w918Eh3fij0")

#movies = [toy_story, avatar, school_of_rock, zootopia, ratatouille, midnight_in_paris, hunger_games]
movies = [zootopia, up, finding_nemo, american_sniper, argo]

fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
