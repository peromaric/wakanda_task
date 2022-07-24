from fastapi import FastAPI
from wakanda_api.router import router as api_router
import wakanda_api.router
import uvicorn
from wakanda_api.web3_interactor import Web3Interactor
from fastapi.middleware.cors import CORSMiddleware


class WakandaAPI:
    def __init__(self):
        self.web3_interactor = Web3Interactor(self)
        self.api: FastAPI = FastAPI(
            title="WakandaVotingAPI",
            description="Votes and stuff"
        )
        wakanda_api.router.web3_interactor = self.web3_interactor
        self.api.include_router(api_router)
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"], #allow frontend to connect
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"], )

        self._run_uvicorn()

    def _run_uvicorn(self) -> None:
        uvicorn.run(self.api, host="0.0.0.0", port=8888)

    def get_api(self) -> FastAPI:
        return self.api
