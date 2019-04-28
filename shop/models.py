from django.db import models
from pytz import timezone
from django.conf import settings
from django.urls import reverse

def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')

    class Meta:
        ordering = ['-id']  # Post 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.name

    def short_desc(self):
        if self.desc:
            t = self.desc[:20] + '...'
        else:
            t = '(리뷰 없음)'
        return t

    short_desc.short_description = '간략 리뷰'

    def tagged(self):
        ts = self.tags.all()
        return '{' + ', '.join(map(str, ts)) + '}'

    tagged.short_description = '태그 집합'

    # 클래스 메소드로 속성을 대신할 때, verbose_name 대신에 short_description

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'

    def get_absolute_url(self):
        # return reverse('blog:post_detail', args=[self.pk])
        return reverse('shop:item_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='아이템')
    message = models.TextField('리뷰')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-item__id', '-id']  # '-post__id', '-id'

    def __str__(self):
        return self.message

    def updated(self):
        return local_time(self.updated_at)

    updated.short_description = '수정 일시'


class Tag(models.Model):
    name = models.CharField('태그', max_length=100, unique=True)

    class Meta:
        ordering = ['-id']  # Tag 객체의 기본 정렬 순서 지정

    def __str__(self):
        return self.name
