from fastapi import APIRouter, HTTPException

from domain.model.order import (
    BuyerId, OrderLineList as DomainOrderLineList, OrderId, OrderAlreadyPaidException, OrderAlreadyCancelledException,
    PaymentNotVerifiedException
)
from domain.model.maps import Address as DomainAddress
from domain import usecase

from rest.schema.order import (
    OrderCreateRequest, OrderCreateResponse, OrderDetail, OrderStatus, OrderUpdateStatusResponse,
)


router = APIRouter()


@router.post('', response_model=OrderCreateResponse)
async def create_order(order: OrderCreateRequest):
    buyer_id = BuyerId(order.buyer_id)
    lines = DomainOrderLineList.deserialize([line.dict() for line in order.lines])
    destination = DomainAddress.deserialize(order.destination.dict())

    order_id = await usecase.create_new_order(buyer_id, lines, destination)

    output = OrderCreateResponse(order_id=str(order_id))
    return output


@router.get('/{order_id}', response_model=OrderDetail)
async def get_order(order_id: str):
    order = await usecase.get_order_from_id(OrderId(order_id))

    output = OrderDetail.from_order(order)
    return output


@router.patch('/{order_id}', response_model=OrderUpdateStatusResponse)
async def update_order_status(order_id: str, status: OrderStatus):
    order_id = OrderId(order_id)

    if status == OrderStatus.paid:
        await _pay_order(order_id)
        return OrderUpdateStatusResponse(order_id=str(order_id), status='paid')

    elif status == OrderStatus.cancelled:
        await _cancel_order(order_id)
        return OrderUpdateStatusResponse(order_id=str(order_id), status='cancelled')

    else:
        error_detail = f'Cannot update Order\'s status to {status}'
        raise HTTPException(status_code=403, detail=error_detail)


async def _pay_order(order_id: OrderId):
    try:
        return await usecase.pay_order(order_id)
    except OrderAlreadyCancelledException:
        error_detail = f'Cannot pay for Order when it\'s already cancelled'
        raise HTTPException(status_code=409, detail=error_detail)
    except OrderAlreadyPaidException:
        error_detail = f'Cannot pay for Order when it\'s already paid'
        raise HTTPException(status_code=409, detail=error_detail)
    except PaymentNotVerifiedException:
        error_detail = f'Payment verification failed'
        raise HTTPException(status_code=403, detail=error_detail)


async def _cancel_order(order_id: OrderId):
    try:
        return await usecase.cancel_order(order_id)
    except OrderAlreadyCancelledException:
        error_detail = f'Cannot cancel Order when it\'s already cancelled'
        raise HTTPException(status_code=409, detail=error_detail)
    except OrderAlreadyPaidException:
        error_detail = f'Cannot cancel Order when it\'s already paid'
        raise HTTPException(status_code=409, detail=error_detail)
