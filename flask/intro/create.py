from app import db, app, Order, Product, Order_Product, Owner, Car, Person

with app.app_context():
    db.drop_all()
    db.create_all()

    user = Person(name="John Doe", username="jdoe", email_address="john.doe@gmail.com", age=25)
    owner = Owner(first_name="John", last_name="Doe")
    test_car = Car(num_plate="LB15 NKP", make="Volkswagen", model="Polo", ownerbr=owner)
    test_car_2 = Car(num_plate="BRY33R", make="BMW", model="530d", ownerbr=owner)
    db.session.add(user)
    db.session.add(owner)
    db.session.add(test_car)
    db.session.commit()

    order = Order(order_number="ABC123")

    db.session.add(order)
    db.session.commit()

    product = Product(product_name="Hat", product_price=12.99, orderbr=order)

    db.session.add(product)
    db.session.commit()

    order_product = Order_Product(order_id=order.id, product_id=product.id, quantity=2)

    db.session.add(order_product)
    db.session.commit()

    test_item = Car.query.filter_by(num_plate="LB15 NKP").first()
    test_item_2 = Car.query.filter_by(num_plate="BRY33R").first()
    print(test_item.ownerbr.first_name)
    print(test_item.num_plate)

    car_to_change = Car.query.filter_by(num_plate="LB15 NKP").first()
    car_to_change.num_plate = "LB16 NKP"
    db.session.commit()

    car_to_delete = Car.query.filter_by(num_plate="LB16 NKP").first()
    db.session.delete(car_to_delete)
    db.session.commit()
    

    # Users.query.filter_by(eye_colour="blue").limit(10).order_by(Users.age.desc()).all()
    