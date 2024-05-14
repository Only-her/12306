from flask import Flask, render_template, request, redirect, jsonify, flash
from datebase import db, User, Order
from db_operations import add_order, delete_order, update_order
from datebase import app  # 确保使用统一的 Flask 实例

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/query_tickets', methods=['GET', 'POST'])
def query_tickets():
    if request.method == 'GET':
        return render_template('query_tickets.html')
    elif request.method == 'POST':
        departure_station = request.form.get('departure_station')
        arrival_station = request.form.get('arrival_station')

        if departure_station and arrival_station:
            orders = Order.query.filter_by(DepartureStation=departure_station, ArrivalStation=arrival_station).all()
        elif departure_station:
            orders = Order.query.filter_by(DepartureStation=departure_station).all()
        elif arrival_station:
            orders = Order.query.filter_by(ArrivalStation=arrival_station).all()
        else:
            orders = Order.query.all()

        return render_template('query_tickets.html', orders=orders)

@app.route('/modify_tickets', methods=['GET', 'POST'])
def modify_tickets():
    if request.method == 'GET':
        return render_template('modify_tickets.html')
    elif request.method == 'POST':
        action = request.form['action']
        try:
            if action == 'Add':
                order = Order(
                    UserID=int(request.form['user_id']),
                    TrainID=int(request.form['train_id']),
                    DepartureStation=request.form['departure_station'],
                    ArrivalStation=request.form['arrival_station'],
                    DepartureTime=request.form['departure_time'],
                    ArrivalTime=request.form['arrival_time'],
                    Quantity=int(request.form['quantity']),
                    TotalPrice=float(request.form['total_price']),
                    Status=request.form['status']
                )
                db.session.add(order)
                db.session.commit()
                flash('Order added successfully!', 'success')
            elif action == 'Delete':
                order = Order.query.get(int(request.form['order_id']))
                if order:
                    db.session.delete(order)
                    db.session.commit()
                    flash('Order deleted successfully!', 'success')
            elif action == 'Update':
                order = Order.query.get(int(request.form['order_id']))
                if order:
                    order.UserID = int(request.form['user_id'])
                    order.TrainID = int(request.form['train_id'])
                    order.DepartureStation = request.form['departure_station']
                    order.ArrivalStation = request.form['arrival_station']
                    order.DepartureTime = request.form['departure_time']
                    order.ArrivalTime = request.form['arrival_time']
                    order.Quantity = int(request.form['quantity'])
                    order.TotalPrice = float(request.form['total_price'])
                    order.Status = request.form['status']
                    db.session.commit()
                    flash('Order updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}', 'error')

        return redirect('/modify_tickets')

# 返回到查询页面路由
@app.route('/back_to_query_tickets')
def back_to_query_tickets():
    return redirect('/query_tickets')

if __name__ == '__main__':
    app.run(debug=True)
