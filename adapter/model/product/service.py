from typing import List, Tuple

from domain.model.product import ProductServiceAbstract, ProductId, PriceThb


class ProductService(ProductServiceAbstract):
    async def total_price(self, product_counts: List[Tuple[ProductId, int]]) -> PriceThb:
        price_list = [PriceThb(15.0) * count for product, count in product_counts]
        return PriceThb(sum(price_list))
