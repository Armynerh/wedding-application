class Base_config:
    SECRET_KEY="00pppgdrfF$"
    ADMIN_EMAIL="amin@gmail.com"
    UPLOAD_FOLDER = 'weddingapp/static/uploads'

class Test_config(Base_config):
    ADMIN_EMAIL='test@yahoo.com'
    

class Live_config(Base_config):
    ADMIN_EMAIL='live@yahoo.com'