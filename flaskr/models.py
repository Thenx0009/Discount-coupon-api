import json
from datetime import datetime, timedelta
import random
import string

DB_FILE = 'flaskr/db.json'

def read_db():
    try:
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Coupon Model: Generate a unique coupon for a product ID and user ID
def generate_coupon(product_id, user_id):
   
    coupon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    expiry_date = datetime.utcnow() + timedelta(hours=1)
    
    coupons = read_db()
    coupon_data = {
        'coupon_code': coupon_code,
        'product_id': product_id,
        'user_id': user_id,
        'expiry_date': expiry_date.isoformat(),
        'valid': True
    }
    
    coupons[coupon_code] = coupon_data
    write_db(coupons)
    
    return coupon_code, expiry_date

# Validate a coupon code for a product and user
def validate_coupon(coupon_code, product_id, user_id):
    coupons = read_db()
    coupon = coupons.get(coupon_code)
    
    if not coupon:
        return False, "Coupon does not exist."
    
    if coupon['product_id'] != product_id:
        return False, "Coupon is not valid for this product."
    
    if coupon['user_id'] != user_id:
        return False, "Coupon is not valid for this user."
    
    expiry_date = datetime.fromisoformat(coupon['expiry_date'])
    if datetime.utcnow() > expiry_date:
        coupon['valid'] = False
        write_db(coupons)
        return False, "Coupon has expired."
    
    return True, "Coupon is valid."
