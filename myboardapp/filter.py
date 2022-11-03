from django_filters import FilterSet, CharFilter  # импортируем filterset
from .models import Comment



# создаём фильтр
class CommentFilter(FilterSet):

    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация
    class Meta:
        model = Comment
        #fields = ('bulletin',)  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)
        fields = {
             'bulletin': ['exact'],
         }
