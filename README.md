# 예비맘 프로젝트 #
산후조리원에 대한 다양한 정보와 신뢰성있는 리뷰를 제공하기 위한 서비스


## Deployment ##

#### 1. Deploy Assets ####
This is first step to deploy new release version of yebimom to existing web server.
Below command uploads static files ( including CSS, JS, Fonts, Images, etc ... ) to S3, 
and creates cached versions of assets ( ex, `yebimom.min.css` -> `css/yebimom.min.023d1297272c.css` )

```
$ python manage.py collectstatic --settings=yebimom.settings.production -v2
```


## 3rd Party Resources ##

For managements app, ( in this case admin theme ) 
manually copy 3rd party resources from Google Drive ( `yebimom/contents/` )

```
yebimom/managements/compontent/

yebimom
├── managements
│   ├── components
```
