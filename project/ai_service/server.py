import os
import connexion

def create_app(test_config=None):
    # create and configure the app
    c_app = connexion.App(__name__, specification_dir="./")
    c_app.add_api('apis.yaml')
    c_app.app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(c_app.app.instance_path, 'ai_service.sqlite'),

    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        c_app.app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        c_app.app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(c_app.app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @c_app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Register init-db an so on.
    # This cannot be from . import db which will cause error
    # The dot will be converted to __main__
    from ai_service import db
    db.init_app(c_app.app)

    return c_app.app

if __name__ == '__main__':
    create_app().run(port=8000, debug=True)