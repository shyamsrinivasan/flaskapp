from flask_login import UserMixin
from app import db, flask_bcrypt
from app import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'test_users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    fullname = db.Column(db.String(40), nullable=False, index=True)
    email = db.Column(db.String(30))
    phone = db.Column(db.String(14))
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(60))
    added_on = db.Column(db.DateTime(timezone=True), nullable=False,
                         server_default=db.func.now())
    added_by = db.Column(db.String(20))
    last_update = db.Column(db.DateTime(timezone=True))
    last_login = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.fullname!r}, username={self.username!r}," \
               f"email={self.email!r}, phone={self.phone!r}," \
               f"last_login={self.last_login!r})"

    def set_password(self, password):
        """hash and set password field to hashed value"""
        # hash password using bcrypt
        hashed = flask_bcrypt.generate_password_hash(password=password.encode('utf-8'),
                                                     rounds=12)
        self.password_hash = hashed

    def set_full_name(self):
        """set value of fullname column using first and last name"""
        self.fullname = self.firstname + ' ' + self.lastname

    def set_added_user(self, change_type, username):
        """set added_user and updated_user"""
        self.added_by = username

    def set_last_login(self):
        """called everytime user obj is called during login"""
        self.last_login = db.func.now()

    def set_last_update(self):
        """called everytime user table
        fields(password/names/contact) are updated"""
        self.last_update = db.func.now()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class UserLog(db.Model):
    __tablename__ = 'test_userlog'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    login_time = db.Column(db.DateTime(timezone=True))


class Customer(UserMixin, db.Model):
    __tablename__ = 'test_customers'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False, index=True)
    lastname = db.Column(db.String(20), nullable=False, index=True)
    fullname = db.Column(db.String(40), index=True)
    type = db.Column(db.Enum('personal', 'commercial', name='customer_type'),
                     nullable=False, index=True)
    date_added = db.Column(db.DateTime(timezone=True), nullable=False,
                           server_default=db.func.now())
    date_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    added_user = db.Column(db.String(20))
    updated_user = db.Column(db.String(20))

    address_info = db.relationship('Address', back_populates='customer_info',
                                   cascade="all, delete", uselist=False)
    identity_info = db.relationship('Identity', back_populates='identity_customer_info',
                                    cascade="all, delete", uselist=False)
    contact_info = db.relationship('Contact', back_populates='contact_customer_info',
                                   cascade="all, delete", uselist=False)
    bill_info = db.relationship('Billing', back_populates='customer_id_info',
                                cascade="all, delete", uselist=False)

    def set_full_name(self):
        """set value of fullname column using first and last name"""
        self.fullname = self.firstname + ' ' + self.lastname

    def set_full_phone(self, country_code, phone_number):
        """set phone number with country code"""
        self.phone = country_code + phone_number

    def set_added_user(self, change_type, username):
        """set added_user and updated_user"""
        if change_type == 'add':
            self.added_user = username
        elif change_type == 'update':
            self.updated_user = username

    def __repr__(self):
        return f"Customer(id={self.id!r}, name={self.fullname!r}, " \
               f"type={self.type!r}, added_on={self.date_added!r})"


class Address(db.Model):
    __tablename__ = 'test_address'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('test_customers.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    customer_name = db.Column(db.String(40), index=True)

    # add address columns from taxdata db table
    type = db.Column(db.Enum('house', 'apartment', 'store-single',
                             'store-complex', name='address_type'), default='house')
    street_num = db.Column(db.String(8))
    street_name = db.Column(db.String(30))
    house_num = db.Column(db.String(8))
    locality = db.Column(db.String(30))
    locality_2 = db.Column(db.String(30))
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(15), nullable=False, server_default='Tamil Nadu')
    pin = db.Column(db.String(6), nullable=False)
    added_user = db.Column(db.String(20))
    date_added = db.Column(db.DateTime(timezone=True), nullable=False,
                           server_default=db.func.now())
    updated_user = db.Column(db.String(20))
    last_update = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    customer_info = db.relationship('Customer', back_populates='address_info',
                                    cascade='all, delete')

    def set_added_user(self, change_type, username):
        """set added_user and updated_user"""
        if change_type == 'add':
            self.added_user = username
        elif change_type == 'update':
            self.updated_user = username

    def __repr__(self):
        return f"Address(id={self.id!r}, customer_id={self.customer_id!r}, " \
               f"name={self.customer_name!r}, locality={self.locality!r}, " \
               f"city={self.city!r}, pin={self.pin!r}, " \
               f"added_on={self.date_added!r})"


class Billing(db.Model):
    __tablename__ = 'test_bills'

    id = db.Column(db.Integer, primary_key=True)
    bill_number = db.Column(db.String(11), nullable=False, index=True)
    customer_name = db.Column(db.String(30), db.ForeignKey('test_customers.fullname',
                                                           onupdate='CASCADE',
                                                           ondelete='CASCADE'),
                              nullable=False, index=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('test_customers.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    pan = db.Column(db.String(10), nullable=False, index=True)
    # bill_date = db.Column(db.DateTime(timezone=True), nullable=False)
    # user_name = db.Column(db.String(40), db.ForeignKey('test_users.fullname', onupdate='CASCADE',
    #                                                    ondelete='CASCADE'), nullable=False)
    # user_name = db.Column(db.String(40), nullable=False)
    items = db.relationship('Items')
    # bill_item = db.Column(db.String(40), nullable=False)
    # price = db.Column(db.Float)
    # quantity = db.Column(db.Integer)
    # item_cost = db.Column(db.Float)

    customer_id_info = db.relationship('Customer', foreign_keys="[Billing.customer_id]",
                                       back_populates='bill_info',
                                       cascade='all, delete')
    customer_name_info = db.relationship('Customer', foreign_keys="[Billing.customer_name]")

    def __repr__(self):
        return f"Billing(id={self.id!r}, name={self.customer_name!r}, " \
               f"bill_no={self.bill_no!r}, cost={self.cost!r})"


class Items(db.Model):
    __tablename__ = 'test_items'

    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.String(11), db.ForeignKey('test_bills.bill_number',
                                                     ondelete='CASCADE'))
    bill_item = db.Column(db.String(40), nullable=False)
    item_cost = db.Column(db.Float)

    def __repr__(self):
        return f"Billing(id={self.id!r}, bill number={self.bill_id!r}, item={self.bill_item!r}, " \
               f"cost={self.item_cost!r})"


class TaxInfo(db.Model):
    __tablename__ = 'test_taxinfo'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('test_customers.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    customer_name = db.Column(db.String(30), index=True)
    filed_by = db.Column(db.String(20), nullable=False, index=True)
    filed_on = db.Column(db.DateTime(timezone=True))


class Identity(db.Model):
    __tablename__ = 'test_identity'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('test_customers.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    customer_name = db.Column(db.String(40), nullable=False)

    dob = db.Column(db.Date, nullable=False)
    pan = db.Column(db.String(10), nullable=False, index=True)
    aadhaar = db.Column(db.String(12))
    added_user = db.Column(db.String(20))
    date_added = db.Column(db.DateTime(timezone=True), nullable=False,
                           server_default=db.func.now())
    updated_user = db.Column(db.String(20))
    last_update = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    identity_customer_info = db.relationship('Customer', back_populates='identity_info',
                                             cascade='all, delete')

    def set_added_user(self, change_type, username):
        """set added_user and updated_user"""
        if change_type == 'add':
            self.added_user = username
        elif change_type == 'update':
            self.updated_user = username

    def __repr__(self):
        return f"Identity(id={self.id!r}, customer_id={self.customer_id!r}, " \
               f"name={self.customer_name!r}, dob={self.dob!r}, " \
               f"pan={self.pan!r}, aadhaar={self.aadhaar!r})"


class Contact(db.Model):
    __tablename__ = 'test_contact'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('test_customers.id', onupdate='CASCADE',
                                                      ondelete='CASCADE'), nullable=False)
    customer_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(30), index=True)
    country_code = db.Column(db.String(4))
    phone = db.Column(db.String(10))

    date_added = db.Column(db.DateTime(timezone=True), nullable=False,
                           server_default=db.func.now())
    date_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    added_user = db.Column(db.String(20))
    updated_user = db.Column(db.String(20))

    contact_customer_info = db.relationship('Customer', back_populates='contact_info',
                                            cascade='all, delete')

    def set_added_user(self, change_type, username):
        """set added_user and updated_user"""
        if change_type == 'add':
            self.added_user = username
        elif change_type == 'update':
            self.updated_user = username

    def __repr__(self):
        return f"Contact(id={self.id!r}, name={self.customer_name!r}, email={self.email!r}, " \
               f"phone={self.country_code + self.phone!r}, added_on={self.date_added!r})"
