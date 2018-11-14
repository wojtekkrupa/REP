'''Testując z użyciem unit testu wszystkie testy umieszczamy w klasie testowej
'''

import unittest

from twitter import Twitter


class TwitterTest(unittest.TestCase):				#każda metoda (rozpoczynająca się od słowa "test" będzie tu testem jednostkowym
	def setUp(self):								#funkcjonalność wywoływana przed każdym z testów gdzi e tworzyny instancję twittera i nie musimy powtarzać kodu
		self.twitter = Twitter()

	def test_initialization(self):						#sprawdzamy czy nasza klasa się tworzy
				                                          #twitter = Twitter()  - bo w setup'ie wiersz 12
		self.assertTrue(self.twitter)					#sprawdzamy czy wartość jest prawdziwa

	def test_tweet_single(self):						#test dodawania wiadomości do listy tweetów
		# Given - sytuacja wejściowa
				#twitter = Twitter()  - bo w setup'ie wiersz 12		#na wejściu jest deklaracja klasy
		# When	- wykonanie akcji na tej sytuacji
		self.twitter.tweet("test jak byk")							#zatweetowanie wiadomości
		# Then	- sprawdzenie wyników assercja
		self.assertEqual(self.twitter.tweets, ["test jak byk"])		#Equal bo sprawdzamy równość między twitter,tweets czyli listą naszych wiadomości a drugim argumentem czyli listą zawierającą naszą wiadomość["...")

if __name__ == '__main__':										#dajemy if aby unittest.main nie wykonał się od razu podczas importu klasy
	unittest.main()													#wykona się w w momencie wywołania całego pliku

# import pytest
#
# from twitter import Twitter
#
# def test_twitter_initialization():
# 	twitter = Twitter()
# 	assert twitter
#
# def test_tweet_single_message():
# 	twitter = Twitter()
# 	twitter.tweet("test jak byk")
# 	assert twitter.tweets == ["test jak byk"]
#
# def test_tweet_long_message():
# 	twitter = Twitter()
# 	#assert twitter
# 	with pytest.raises(Exception):
# 		twitter.tweet("test" *41)
# 	assert twitter.tweets == []
#
# def tweet_with_hashtags():
# 	twitter = Twitter()
# 	wiadomosc = "test #first message"
# 	twitter.tweet(wiadomosc)
# 	assert "first" in twitter.find_hashtags()