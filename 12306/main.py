from datebase import app, db
from web_server import app as web_server_app  # 确保导入 web_server 中的路由

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
