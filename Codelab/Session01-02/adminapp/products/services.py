from products.repositories import ProductRepository
from products.models import Product

class ProductService:
    @staticmethod
    def get_all_products():
        return ProductRepository.get_all()

    @staticmethod
    def get_product_by_id(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def create_product(name, price, description):
        product = Product(name=name, price=price, description=description)
        ProductRepository.create(product)
        return product

    @staticmethod
    def update_product(product_id, name, price, description):
        product = ProductRepository.get_by_id(product_id)
        if product:
            product.name = name
            product.price = price
            product.description = description
            ProductRepository.update()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = ProductRepository.get_by_id(product_id)
        if product:
            ProductRepository.delete(product)
            return True
        return False