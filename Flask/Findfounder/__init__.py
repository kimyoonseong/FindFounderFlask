from flask import Flask
import os

 #Flask 어플리케이션을 생성하는 코드
# 이 파일에 다른 파일 경유 없이 test.py를 통해 실행된다면 __name__ 변수에는 'test'라는 문자열이 담김

# URL과 FLASK코드를 매핑하는 Flask 데코레이터
def create_app():
    app = Flask(__name__)
    # app.config['TF_ENABLE_ONEDNN_OPTS'] = '0'
    os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app


