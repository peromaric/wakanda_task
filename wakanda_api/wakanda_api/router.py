from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional
from wakanda_api.web3_interactor import Web3Interactor
import random

"""
router with its .get and .post routes below.
include this router in a fastapi instance.
"""
router: InferringRouter = InferringRouter()
web3_interactor: Optional[Web3Interactor] = None


@router.get(
    "/",
    summary="Home Page"
)
async def home():
    response: RedirectResponse = RedirectResponse(url="/redoc")  # redirect to interface
    return response


"""
Returns just the balance from the contract
"""


class Balance(BaseModel):
    x: int
    y: int


@router.get(
    "/balance_of",
    response_model=Balance,
    summary="Returns contract balance"
)
async def get_balance_of():
    return await web3_interactor.balance_of("0x5FbDB2315678afecb367f032d93F642f64180aa3")

