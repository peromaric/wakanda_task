from fastapi import FastAPI
import wakanda_api.router
from wakanda_api.router import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


class WakandaAPI:
    def __init__(self):
        self.api: FastAPI = FastAPI(
            title="WakandaVotingAPI",
            description="Votes and stuff"
        )
        self.api.include_router(router)
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
