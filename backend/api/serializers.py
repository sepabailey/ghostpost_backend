from rest_framework import serializers
from backend.api.models import Post

# Source to help with serializers: https://www.youtube.com/watch?v=dQw4w9WgXcQ


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post_title', 'body', 'date', 'upvotes',
                  'downvotes', 'results', 'boast_or_roast']

    def results(self):
        return self.upvotes - self.downvotes
