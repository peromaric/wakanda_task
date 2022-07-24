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


@router.get(
    "/balance_of/{address}",
    summary="Returns contract balance"
)
async def get_balance_of(address):
    response = await web3_interactor.balance_of(address)
    return response


"""
Registered voter
"""


@router.get(
    "/register_voter/{address}",
    summary="Returns transaction hash"
)
async def register_voter(address):
    response = await web3_interactor.register_voter(address)
    return response


@router.get(
    "/vote/{voter_address}_{candidate_address}",
    summary="Returns True if successful"
)
async def vote(voter_address, candidate_address):
    response = await web3_interactor.vote(voter_address, candidate_address)
    return response


@router.get(
    "/candidate_list/",
    summary="Returns the list of candidates"
)
async def candidate_list():
    return await web3_interactor.candidate_list()

