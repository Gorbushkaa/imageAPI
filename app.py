from flask import Flask, request
from celery import Celery
from PIL import Image

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'mongodb://localhost:27017/database_name'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://localhost:27017/database_name'
celery = Celery(app.name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def background_task(height, width):
    a = height + width
    print(a)

"""    print('112')
    original_image = Image.open("D:/Python/Проекты/imageapi" + name)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(name+name)

    scaled_image = Image.open(name)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    return 'Hellooo'"""



@app.route('/api/', methods=['POST'])
def image():
    content = request.json
    background_task.delay(content['h'], content['w'], content['name'])
    return 'dd'


if __name__ == '__main__':
    app.run(debug=True)