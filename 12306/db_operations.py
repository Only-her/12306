from datebase import db, Order

def add_order(user_id, train_id, departure_station, arrival_station, departure_time, arrival_time, quantity, total_price, status):
    order = Order(
        UserID=user_id,
        TrainID=train_id,  # 添加 TrainID
        DepartureStation=departure_station,
        ArrivalStation=arrival_station,
        DepartureTime=departure_time,
        ArrivalTime=arrival_time,
        Quantity=quantity,
        TotalPrice=total_price,
        Status=status
    )

    db.session.add(order)
    db.session.commit()

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return True
    else:
        return False

def update_order(order_id, new_status):
    order = Order.query.get(order_id)
    if order:
        order.Status = new_status
        db.session.commit()
        return True
    else:
        return False
