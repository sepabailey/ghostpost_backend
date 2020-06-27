from django.shortcuts import render, HttpResponseRedirect
from rest_framework import viewsets
from backend.api.serializers import PostSerializer
from backend.api.models import Post
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.api.forms import AddPostForm


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Peter helped to understand setting up actions correctly
    @action(detail=False)
    def boast(self, request):
        boast = Post.objects.filter(boast_or_roast=True).order_by('-date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roast(self, request):
        roast = Post.objects.filter(boast_or_roast=False).order_by('-date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.upvotes += 1
        post.save()
        return Response('success')

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=id):
        post = Post.objects.get(pk=pk)
        post.downvotes += 1
        post.save()
        return Response('success')

    @action(detail=False)
    def highestvote(self, request):
        highestvotes = Post.objects.all().order_by('-upvotes', 'downvotes')
        serializer = self.get_serializer(highestvotes, many=True)
        return Response(serializer.data)


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            newpost = form.cleaned_data
            Post.objects.create(
                post_title=newpost['post_title'],
                body=newpost['body'],
                boast_or_roast=newpost['boast_or_roast'],
            )
            return HttpResponseRedirect('http://localhost:3000/')
    form = AddPostForm()
    return render(request, 'addpost.html', {'form': form})
