from django.test import TestCase
from django.urls import reverse

from .models import Place

##A Test to check if the home page shows an empty list by asserting if the template is used and asserting false if places is empty
class TestViewHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])

#A test to check if the correct template was used and assert it is the same as the ones in the fictures.json
class TestWishList(TestCase):
    fixtures =  ['test_places']

    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        data_rendered = list(response.context['places'])

        data_expected = list(Place.objects.filter(visited=False))

        self.assertCountEqual(data_rendered, data_expected)