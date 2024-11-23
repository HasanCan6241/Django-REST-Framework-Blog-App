from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,viewsets
from posts.models import Post,Tag, Author
from posts.serializers import TagSerializer,AuthorSerializer, PostSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

# APIView low-level
# Generic Views sık kullanılan view işlevsellikleri sınıflar aracılığı ile önceden tanımlanmış
# ViewSet high-level

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



"""class PostView(APIView):

    def get(self,request):

        posts = Post.objects.all()

        serializer=PostSerializer(posts,many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer=PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)"""

"""class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
"""

"""class PostDetailView(APIView):
    def get(self,request,id): # kaydı görüntülemek için
        post=get_object_or_404(Post,id=id)
        serializer=PostSerializer(post)

        return Response(serializer.data)

    def put(self,request,id): # kaydın tamamını güncellemek için 
        post=get_object_or_404(Post,id=id)
        serializer=PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save() #update metodunu arayacak
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,id): # kaydın kısmi olarak güncellenmesi
        post=get_object_or_404(Post,id=id)
        serializer=PostSerializer(post,data=request.data,partial=True) # kısmi güncelleme için partial yani tüm alanları güncellemek zorunda değiliz
        if serializer.is_valid():
            serializer.save() #update metodunu arayacak put ile ortak metotu kullanıyorlar
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id): # kaydın silinmesi
        post = get_object_or_404(Post, id=id)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)"""

"""# python model nesnelerini serializer ile json formatına dönüştürüyoruz
class TagView(APIView):

    def get(self,request):

        tags = Tag.objects.all()

        serializer = TagSerializer(tags,many=True) #many argümanı verinin çoğul olduğunu gösteriyor

        return Response(serializer.data)

    def post(self,request):

        serializer= TagSerializer(data=request.data) # post ile gelen bilgiyi ithiyacımız olan formata çevirip, istediğimiz alanlar ile uyumluluğunu kontrol ediyoruz

        if serializer.is_valid(): # alına verinin doğru formatta olduğunu kontrol ediyoruz
            serializer.save() # veri tabanına kaydeder
            return Response(serializer.data,status=status.HTTP_200_OK) # kaydettiğimiz kaydı döndürüyoruz. status boş geçerşe 200 döner

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # hata alınırsa errors içine hatalar kaydediliyor ve status ile hatayı kodunu döndürüyoruz"""

"""class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
"""
"""class AuthorView(APIView):

    def get(self,request):

        authors=Author.objects.all()
        serializer=AuthorSerializer(authors,many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer=AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)"""


"""class AuthorView(generics.ListCreateAPIView): # listcrete kaynağın hem listelenmesi hemde yeni kayıtların oluşmasını sağlar
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer"""

