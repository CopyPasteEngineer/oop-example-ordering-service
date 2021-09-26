from fastapi import APIRouter

from domain.model.order import BuyerId, OrderLineList as DomainOrderLineList, OrderId
from domain.model.maps import Address as DomainAddress

from rest.schema.order import OrderCreateRequest, OrderCreateResponse, OrderDetail
from rest.dependency import get_order_service, get_order_repository


router = APIRouter()


@router.get('', response_model=OrderDetail)
async def get_order(id: str, order_repository=get_order_repository()):
    order_id = OrderId(id)

    order = await order_repository.from_id(order_id)

    output = OrderDetail.from_order(order)
    return output


@router.post('', response_model=OrderCreateResponse)
async def create_order(order: OrderCreateRequest, order_service=get_order_service()):
    buyer_id = BuyerId(order.buyer_id)
    lines = DomainOrderLineList.deserialize([line.dict() for line in order.lines])
    destination = DomainAddress.deserialize(order.destination.dict())

    order_id = await order_service.new_order(buyer_id=buyer_id, lines=lines, destination=destination)

    output = OrderCreateResponse.from_order_id(order_id)
    return output
