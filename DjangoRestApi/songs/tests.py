from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer


class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_song(title="", artist=""):
		if title !="" and artist !="":
			Songs.objects.create(title=title, artist=artist)

	def setUp(self):
		self.create_song("like glue", "sean paul")
		self.create_song("Story of my life", "one direction")
class GetAllSongsTest(BaseViewTest):
	def test_get_all_songs(self):
		"""
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
		response = self.client.get(
					reverse("songs-all", kwargs={"Version": "v1"})
			)

		expected = Songs.objects.all()
		serialized = SongsSerializer(expected, many=True)
		self.assertEquel(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)