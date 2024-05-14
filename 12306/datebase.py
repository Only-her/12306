from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/12306'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123456'

db = SQLAlchemy(app)

# 数据库模型定义
class User(db.Model):
    __tablename__ = 'users'

    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    Phone = db.Column(db.String(20), unique=True, nullable=False)
    FullName = db.Column(db.String(255))
    IDNumber = db.Column(db.String(20))

    def __repr__(self):
        return f'<User {self.Username}>'

# 定义订单模型
class Order(db.Model):
    __tablename__ = 'orders'

    OrderID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer)
    TrainID = db.Column(db.Integer)
    DepartureStation = db.Column(db.String(255))
    ArrivalStation = db.Column(db.String(255))
    DepartureTime = db.Column(db.String(255))
    ArrivalTime = db.Column(db.String(255))
    Quantity = db.Column(db.Integer)
    TotalPrice = db.Column(db.Float)
    Status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Order {self.OrderID}>'

# 定义支付模型
class Payment(db.Model):
    __tablename__ = 'payments'

    PaymentID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey('orders.OrderID'), nullable=False)
    PaymentTime = db.Column(db.DateTime, nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    PaymentMethod = db.Column(db.String(50), nullable=False)

    order = db.relationship('Order', backref=db.backref('payments', lazy=True))

    def __repr__(self):
        return f'<Payment {self.PaymentID}>'
