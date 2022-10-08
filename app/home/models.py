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
    username = db.Column(db.String(20), nullable=False, index=True)
    password_hash = db.Column(db.String(60))
    added_on = db.Column(db.DateTime(timezone=True), nullable=False,
                         server_default=db.func.now())
    added_by = db.Column(db.String(20))

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, firstname={self.firstname!r}," \
               f"lastname={self.lastname!r}, email={self.email!r}, phone={self.phone!r}," \
               f"username={self.username!r})"

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


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Customer(UserMixin, db.Model):
    __tablename__ = 'test_customers'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False, index=True)
    lastname = db.Column(db.String(20), nullable=False, index=True)
    fullname = db.Column(db.String(40), index=True)
    email = db.Column(db.String(30), index=True)
    phone = db.Column(db.String(14))
    type = db.Column(db.Enum('personal', 'commercial', name='customer_type'),
                     nullable=False, index=True)
    date_added = db.Column(db.DateTime(timezone=True), nullable=False,
                           server_default=db.func.now())
    date_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())
    added_user = db.Column(db.String(20))
    updated_user = db.Column(db.String(20))

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
        return f"Customer(id={self.id!r}, name={self.fullname!r}, email={self.email!r}, " \
               f"phone={self.phone!r}, type={self.type!r}, added_on={self.date_added!r})"
