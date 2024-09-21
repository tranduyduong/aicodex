from flask import Blueprint, request, jsonify
from products.services import ProductService

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
def create_product_route():
    data = request.get_json()
    new_product = ProductService.create_product(data['name'], data['price'], data.get('description'))
    return jsonify({'message': 'Product created successfully', 'product': {'id': new_product.id, 'name': new_product.name, 'price': new_product.price, 'description': new_product.description}}), 201

@products_bp.route('/products', methods=['GET'])
def get_products_route():
    products = ProductService.get_all_products()
    return jsonify([{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description} for product in products])

@products_bp.route('/products/<int:id>', methods=['GET'])
def get_product_route(id):
    product = ProductService.get_product_by_id(id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description})

@products_bp.route('/products/<int:id>', methods=['PUT'])
def update_product_route(id):
    data = request.get_json()
    updated_product = ProductService.update_product(id, data['name'], data['price'], data.get('description'))
    return jsonify({'message': 'Product updated successfully', 'product': {'id': updated_product.id, 'name': updated_product.name, 'price': updated_product.price, 'description': updated_product.description}})

@products_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product_route(id):
    ProductService.delete_product(id)
    return jsonify({'message': 'Product deleted successfully'})