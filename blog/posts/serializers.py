from rest_framework import serializers
from posts.models import Tag,Author,Post
from django.shortcuts import get_object_or_404

# serializers model objelerini jsn formatında dönüştürmek için kullanılan bir bileşen

"""class TagSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True) # Apı get atarak listelemek istersek ıd lerde gelicek. Post isteği yaptığımızda id özelliğini gönderemeye gerek kalmıyor
    name= serializers.CharField(max_length=50)

    def create(self, validated_data): #create, serializer ile gelen özel bir metot. veriyi kaydedetmek istediğimizde bu metot çalışacak
        #return Tag.objects.create(name=validated_data.get('name'))Çok fazla özellik olduğunda bunu kullanmak mantıklı olmayabilir
        # .buradaki create veri tabanında yeni bir nesne oluşturmak için farklı bir metot
        return Tag.objects.create(**validated_data)"""

class TagSerializer(serializers.ModelSerializer): # create ve update kaynak kodda oluşturuluyor
    class Meta:
        model=Tag
        fields='__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

"""class AuthorSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name= serializers.CharField(max_length=100)
    surname=serializers.CharField(max_length=100)
    age=serializers.IntegerField()
    email=serializers.EmailField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
        # **validation_data, validated_data sözlüğündeki key-value çifterinin çağırdığımız metota ayrı ayrı argümanlar olarak gönderilmesini sağlayan bir kısayol"""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'

"""class PostSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=50)
    content=serializers.CharField()
    created=serializers.DateTimeField(read_only=True)
    updated=serializers.DateTimeField(read_only=True)
    is_published=serializers.BooleanField()

    author=AuthorSerializer(read_only=True)
    tags=TagSerializer(many=True,required=False,read_only=True) # biz tags argümanını blank=true yaptığımız için required argümanı ile tags olmasada kaydetmeyi sağlat

    author_id=serializers.IntegerField(write_only=True) #sadece yazma işlemi yaptığımız metotlarda gerektiğini belirtiyor

    tag_ids=serializers.ListField(            #tag grup olarak geleceği için
        child=serializers.IntegerField(),
        write_only=True,
        required=False #false olduğu için get isteğinde görmüyoruz
    )

    def create(self, validated_data): #serializer.save() ile çalışıyor
        author_id=validated_data.pop("author_id")
        tag_ids = validated_data.pop("tag_ids", [])  # [] key bulamazsa boş dönmesini sağlar. Boşta olabileceği için [] bu şekilde yazdık

        author = get_object_or_404(Author, pk=author_id)
        post=Post.objects.create(author=author,**validated_data)

        #tags ve post arasında many to many olduğu için django ara tablo oluşturarak yapıyor

        if tag_ids:
            tags=Tag.objects.filter(id__in=tag_ids)
            post.tags.set(tags)

        return post

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title) # instance.title, eğer title güncellemezsek varsayılan değeri verir
        instance.content=validated_data.get('content',instance.content)
        instance.is_published=validated_data.get('is_published',instance.is_published)

        author_id=validated_data.get('author_id')
        if author_id:

            author=get_object_or_404(Author,id=author_id)
            instance.author=author

        tag_ids=validated_data.get('tag_ids',[])
        if tag_ids:
            instance.tags.clear()
            tags=Tag.objects.filter(id__in=tag_ids)
            instance.tags.set(tags)

        instance.save()

        return instance"""