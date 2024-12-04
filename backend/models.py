from config import db

class coil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    quantity = db.Column(db.Float , nullable=False)
    date_to_deliver = db.Column(db.String(100) , nullable=False)
    order_recived_date = db.Column(db.String(100) , nullable=False)
    wire_guage = db.Column(db.String(100) , nullable=False)
    net_weight = db.Column(db.Float , nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'date_to_deliver': self.date_to_deliver,
            'order_recived_date': self.order_recived_date,
            'wire_guage': self.wire_guage,
            'net_weight': self.net_weight
        }
    
class past_coil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    quantity = db.Column(db.Float , nullable=False)
    date_to_deliver = db.Column(db.String(100) , nullable=False)
    date_on_delivered = db.Column(db.String(100) , nullable=False)
    order_recived_date = db.Column(db.String(100) , nullable=False)
    wire_guage = db.Column(db.String(100) , nullable=False)
    net_weight = db.Column(db.Float , nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'date_to_deliver': self.date_to_deliver,
            'date_on_delivered': self.date_on_delivered,
            'order_recived_date': self.order_recived_date,
            'wire_guage': self.wire_guage,
            'net_weight': self.net_weight
        }
    
class wire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    quantity = db.Column(db.Float , nullable=False)
    wire_recived_date = db.Column(db.String(100) , nullable=False)
    wire_guage = db.Column(db.String(100) , nullable=False)
    net_weight = db.Column(db.Float , nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'wire_recived_date': self.wire_recived_date,
            'wire_guage': self.wire_guage,
            'net_weight': self.net_weight
        }
    
class past_wire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False)
    quantity = db.Column(db.Float , nullable=False)
    wire_recived_date = db.Column(db.String(100) , nullable=False)
    wire_guage = db.Column(db.String(100) , nullable=False)
    net_weight = db.Column(db.Float , nullable=False)
    date_on_delivered = db.Column(db.String(100) , nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'wire_recived_date': self.wire_recived_date,
            'wire_guage': self.wire_guage,
            'net_weight': self.net_weight,
            'date_on_delivered': self.date_on_delivered
        }