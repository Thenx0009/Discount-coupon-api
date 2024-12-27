from flask import Blueprint, jsonify, request
from flaskr.models import generate_coupon, validate_coupon

bp = Blueprint('coupon', __name__)

# Endpoint to generate a discount coupon for a product
# @bp.route('/generate-coupon', methods=['POST'])
# def generate_coupon_for_product():
#     data = request.get_json()
#     product_id = data.get('product_id')
    
#     if not product_id:
#         return jsonify({"error": "Product ID is required"}), 400
    
#     coupon_code, expiry_date = generate_coupon(product_id)
    
#     return jsonify({
#         "message": "Coupon generated successfully.",
#         "coupon_code": coupon_code,
#         "expiry_date": expiry_date.isoformat()
#     }), 201

# # Endpoint to validate the discount coupon
# @bp.route('/validate-coupon', methods=['POST'])
# def validate_coupon_for_product():
#     data = request.get_json()
#     coupon_code = data.get('coupon_code')
#     product_id = data.get('product_id')
    
#     if not coupon_code or not product_id:
#         return jsonify({"error": "Coupon code and product ID are required"}), 400
    
#     is_valid, message = validate_coupon(coupon_code, product_id)
    
#     if is_valid:
#         return jsonify({"message": "Coupon is valid."}), 200
#     else:
#         return jsonify({"error": message}), 400
# Endpoint to generate a discount coupon for a product and user
@bp.route('/generate-coupon', methods=['POST'])
def generate_coupon_for_product():
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    
    if not product_id or not user_id:
        return jsonify({"error": "Product ID and User ID are required"}), 400
    
    coupon_code, expiry_date = generate_coupon(product_id, user_id)
    
    return jsonify({
        "message": "Coupon generated successfully.",
        "coupon_code": coupon_code,
        "expiry_date": expiry_date.isoformat()
    }), 201

# Endpoint to validate the discount coupon for a product and user
@bp.route('/validate-coupon', methods=['POST'])
def validate_coupon_for_product():
    data = request.get_json()
    coupon_code = data.get('coupon_code')
    product_id = data.get('product_id')
    user_id = data.get('user_id')
    
    if not coupon_code or not product_id or not user_id:
        return jsonify({"error": "Coupon code, Product ID, and User ID are required"}), 400
    
    is_valid, message = validate_coupon(coupon_code, product_id, user_id)
    
    if is_valid:
        return jsonify({"message": "Coupon is valid."}), 200
    else:
        return jsonify({"error": message}), 400
