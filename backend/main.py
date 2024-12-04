from config import app 
from models import coil, past_coil , wire , past_wire
from flask import request, jsonify
from config import db

@app.route('/coils', methods=['GET'])
def get_coils():
    Coils = coil.query.all()
    json_coils = list(map(lambda x: x.to_json(), Coils))
    return jsonify(json_coils)

@app.route('/create_coils', methods=['POST'])
def create_coils():
    # geting data from request
    data = request.get_json()
    coil_name = data.get('name')
    coil_quantity = data.get('quantity')
    coil_date_to_deliver = data.get('date_to_deliver')
    coil_order_recived_date = data.get('order_recived_date')
    coil_wire_guage = data.get('wire_guage')
    coil_net_weight = data.get('net_weight')
    # creating new coil
    new_coil = coil(name=coil_name, quantity=coil_quantity, date_to_deliver=coil_date_to_deliver, order_recived_date=coil_order_recived_date, wire_guage=coil_wire_guage, net_weight=coil_net_weight)
    if not coil_name or not coil_quantity or not coil_date_to_deliver or not coil_order_recived_date or not coil_wire_guage or not coil_net_weight:
        return jsonify({'error': 'Please provide all details'}), 400
    try:
        db.session.add(new_coil)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    #final responce
    return jsonify({'message': 'New coil created!'}) , 201

@app.route('/delete_coils', methods=['DELETE'])
def delete_coils():
    data = request.get_json()
    coil_id = data.get('id')
    if not coil_id:
        return jsonify({'error': 'Please provide coil id'}), 400
    coil_to_delete = coil.query.filter_by(id=coil_id).first()
    if not coil_to_delete:
        return jsonify({'error': 'Invalid coil id'}), 400
    db.session.delete(coil_to_delete)
    db.session.commit()
    return jsonify({'message': 'Coil deleted!'})

@app.route('/update_coils', methods=['PUT'])
def update_coil():
    data = request.get_json()
    coil_id = data.get('id')
    coil_name = data.get('name')
    coil_quantity = data.get('quantity')
    coil_date_to_deliver = data.get('date_to_deliver')
    coil_order_recived_date = data.get('order_recived_date')
    coil_wire_guage = data.get('wire_guage')
    coil_net_weight = data.get('net_weight')
    if not coil_id:
        return jsonify({'error': 'Please provide coil id'}), 400
    coil_to_update = coil.query.filter_by(id=coil_id).first()
    if not coil_to_update:
        return jsonify({'error': 'Invalid coil id'}), 400
    coil_to_update.name = coil_name
    coil_to_update.quantity = coil_quantity
    coil_to_update.date_to_deliver = coil_date_to_deliver
    coil_to_update.order_recived_date = coil_order_recived_date
    coil_to_update.wire_guage = coil_wire_guage
    coil_to_update.net_weight = coil_net_weight
    db.session.commit()
    return jsonify({'message': 'Coil updated!'})

@app.route('/move_coil', methods=['POST'])
def move_coil():
    data = request.get_json()
    coil_id = data.get('id')
    delivered_on_date = data.get('delivered_on_date')
    if not coil_id or not delivered_on_date:
        return jsonify({'error': 'Please provide coil id and delivered on date'}), 400
    coil_to_move = coil.query.filter_by(id=coil_id).first()
    if not coil_to_move:
        return jsonify({'error': 'Invalid coil id'}), 400
    past_coil_data = {
        'name': coil_to_move.name,
        'quantity': coil_to_move.quantity,
        'date_to_deliver': coil_to_move.date_to_deliver,
        'order_recived_date': coil_to_move.order_recived_date,
        'wire_guage': coil_to_move.wire_guage,
        'net_weight': coil_to_move.net_weight,
        'delivered_on_date': delivered_on_date
    }
    new_past_coil = past_coil(**past_coil_data)
    try:
        db.session.add(new_past_coil)
        db.session.delete(coil_to_move)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Coil moved to past_coil table!'})

@app.route('/wire', methods=['GET'])
def get_wire():
    Wires = wire.query.all()
    json_wires = list(map(lambda x: x.to_json(), Wires))
    return jsonify(json_wires)

@app.route('/create_wire', methods=['POST'])
def create_wire():
    data = request.get_json()
    wire_name = data.get('name')
    wire_quantity = data.get('quantity')
    wire_recived_date = data.get('wire_recived_date')
    wire_guage = data.get('wire_guage')
    wire_net_weight = data.get('net_weight')
    new_wire = wire(name=wire_name, quantity=wire_quantity, wire_recived_date=wire_recived_date, wire_guage=wire_guage, net_weight=wire_net_weight)
    if not wire_name or not wire_quantity or not wire_recived_date or not wire_guage or not wire_net_weight:
        return jsonify({'error': 'Please provide all details'}), 400
    try:
        db.session.add(new_wire)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'New wire created!'}), 201

@app.route('/delete_wire', methods=['DELETE'])
def delete_wire():
    data = request.get_json()
    wire_id = data.get('id')
    if not wire_id:
        return jsonify({'error': 'Please provide wire id'}), 400
    wire_to_delete = wire.query.filter_by(id=wire_id).first()
    if not wire_to_delete:
        return jsonify({'error': 'Invalid wire id'}), 400
    db.session.delete(wire_to_delete)
    db.session.commit()
    return jsonify({'message': 'Wire deleted!'})

@app.route('/update_wire', methods=['PUT'])
def update_wire():
    data = request.get_json()
    wire_id = data.get('id')
    wire_name = data.get('name')
    wire_quantity = data.get('quantity')
    wire_recived_date = data.get('wire_recived_date')
    wire_guage = data.get('wire_guage')
    wire_net_weight = data.get('net_weight')
    if not wire_id:
        return jsonify({'error': 'Please provide wire id'}), 400
    wire_to_update = wire.query.filter_by(id=wire_id).first()
    if not wire_to_update:
        return jsonify({'error': 'Invalid wire id'}), 400
    wire_to_update.name = wire_name
    wire_to_update.quantity = wire_quantity
    wire_to_update.wire_recived_date = wire_recived_date
    wire_to_update.wire_guage = wire_guage
    wire_to_update.net_weight = wire_net_weight
    db.session.commit()
    return jsonify({'message': 'Wire updated!'})

@app.route('/move_wire', methods=['POST'])
def move_wire():
    data = request.get_json()
    wire_id = data.get('id')
    delivered_on_date = data.get('delivered_on_date')
    if not wire_id or not delivered_on_date:
        return jsonify({'error': 'Please provide wire id and delivered on date'}), 400
    wire_to_move = wire.query.filter_by(id=wire_id).first()
    if not wire_to_move:
        return jsonify({'error': 'Invalid wire id'}), 400
    past_wire_data = {
        'name': wire_to_move.name,
        'quantity': wire_to_move.quantity,
        'wire_recived_date': wire_to_move.wire_recived_date,
        'wire_guage': wire_to_move.wire_guage,
        'net_weight': wire_to_move.net_weight,
        'delivered_on_date': delivered_on_date
    }
    new_past_wire = past_wire(**past_wire_data)
    try:
        db.session.add(new_past_wire)
        db.session.delete(wire_to_move)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'message': 'Wire moved to past_wire table!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) # run our app in debug mode




