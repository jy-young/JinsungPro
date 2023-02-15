from django.db import models

class Post(models.Model):
    product_photo = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = [
        '파리,파리나방 채집',
        '수고,경사각,방위측정',
        '수목 직경측정',
        '수목 연륜측정 및 분석',
        '수목 기타측정 및 진단',
        '야외조사 보조용품',
        '곤충 채집',
        '곤충 분류,전시,보관',
        '식물 채집,보관',
        '병해충 방제기구',
        '기타',
    ]
    all_tags = [(item,item) for item in tags]
    tag = models.CharField(max_length=30, choices=all_tags, default=all_tags[10])
