from app.models import Review, User
from app import db


def setUp(self):

    self.user_Erick = User(username = 'Erick', password = 'potato', email = 'erick@mutua.com')

    self.new_review = Review(movie_id = 1234, movie_title = 'movie', image_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', movie_review = 'best 12 hors of my life', user = self.user_Erick)


def tearDown(self):

    Review.query.delete()

    User.query.delete()


def test_check_instance_variables(self):
    self.assertEquals(self.new_review.movie_id, 1234)
    self.assertEquals(self.new_review.movie_title, 'movi')
    self.assertEquals(self.new_review.image_path, "https://image.tmdb.org/t/p/w500/jdjdjdjn")
    self.assertEquals(self.new_review.movie_review, 'best 12 hors of my life')
    self.assertEquals(self.new_review.user, self.user_Erick)


def test_save_review(self):
    self.new_review.save_review()
    self.assertTrue(len(Review.query.all()) > 0)


def test_get_review_by_id(self):
    self.new_review.save_review()
    got_reviews = Review.get_reviews(12345)
    self.assertTrue(len(got_reviews) == 1)
