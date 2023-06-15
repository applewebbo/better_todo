from django.urls import reverse


class TestIndex:
    def test_unauthenticated(self, client):
        """A unauthenticated user gets a valid response"""
        response = client.get(reverse("main:index"))

        assert response.status_code == 200
