from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from typing import Optional, List
from wakanda_api.web3_interactor import Web3Interactor
from fastapi import HTTPException, Response, status

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


class VoteCast(BaseModel):
    voterAddress: str
    candidateAddresses: List[str]


@router.post(
    "/vote/",
    summary="Returns True if successful",
    status_code=200
)
async def vote(vote_cast: VoteCast):
    vote_success = await web3_interactor.vote(vote_cast.voterAddress, vote_cast.candidateAddresses)
    if vote_success:
        return vote_success
    else:
        raise HTTPException(status_code=404, detail="Couldn't cast vote")


@router.get(
    "/candidate_list/",
    summary="Returns the list of candidates"
)
async def candidate_list():
    return await web3_interactor.candidate_list()

