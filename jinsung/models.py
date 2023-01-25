from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = [
        '위치,거리,고도측정',
        '수고,경사각,방위측정',
        '수목 직경측정',
        '수목 연륜측정 및 분석',
        '수목 기타측정 및 진단',
        '야외조사 보조용품',
        '토양 조사,채취,분석',
        '수목 생장,배양,발아,건조기기',
        '양묘용기,종묘,육립',
        '대기오염측정,기상관측',
        '곤충 채집',
        '곤충 분류,전시,보관',
        '곤충 사육,추출,야생동물',
        '식물 채집,보관',
        '병해충 방제기구',
        '다용도기구',
        '기타',
    ]
    all_tags = [(item,item) for item in tags]
    tag = models.CharField(max_length=30, choices=all_tags, default=all_tags[16])
