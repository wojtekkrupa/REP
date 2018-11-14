# int
lesson_number = 1
print(lesson_number, type(lesson_number))

# string

lesson_name = 'pyton'

print(lesson_name, type(lesson_name))

# list

tweet_lenghts = [140, 80, 20, 105, "rekscik",]

print(tweet_lenghts, type(tweet_lenghts))
print(tweet_lenghts[1])
tweet_lenghts[1] = 81
print(tweet_lenghts[1])

# tuple

tweet_lenghts_immutable = (140, 80, 20, 105, "rekscik")

print(tweet_lenghts_immutable, type(tweet_lenghts_immutable))

# dict

tweets_by_user = {
	'Jonh_klucz': [1, 15],
	'Mary_klucz': [2, 5]
}
print(tweets_by_user, type(tweets_by_user))
print(tweets_by_user['Jonh_klucz'])

x = ['test']
if type(x) == int:
	print("This is int")
elif type(x) == str:
	print("This is str")

else:
	print("I don't know")

for tweet in tweet_lenghts:
	print(tweet)
	print("test")

def print_line():
	print("=========")

print_line()


def type_print(wartosc):
	print(wartosc, type(wartosc))

type_print(1)


def custom_print(wartosc, list_wartosc=None, *args, **kwargs):
	"""

	:param wartosc:
	:param list_wartosc:
	:param args:	WSZYSTKIE POZOSTAŁE ARGUMENTY
	:param kwargs: 	wszystkie pozostałe arumenty kluczowe - key words arguments
	"""
	print("POCZĄTEK")
	print("VARTOŚĆ", wartosc)
	if list_wartosc:
		for element in list_wartosc:
			print("LIST VARTOŚĆ", element)
	print("ARGS", args)
	print("KWARGS", kwargs)

	print("KONIEC")

custom_print(1)
custom_print(1, [1, 2, 3], )
print("_______________")
custom_print(1, [1, 2, 3], 'arg3', 3, arg5 = 1, arg6 = {'test':'bla'})	# arg3 i 3 wezły jako tupla, z "=" argument nazwany i wejdzie do słownika arg5 jako klucz i 1 jako wartość

