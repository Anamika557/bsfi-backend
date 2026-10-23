
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.solution import SolutionCreate, SolutionResponse
from app.services import solution_service

router = APIRouter(prefix="/solutions", tags=["Solutions"])


class SolutionAPI:

    def create_solution(
        self,
        solution: SolutionCreate,
        db: Session = Depends(get_db)
    ):
        return solution_service.create_solution_service(db, solution)

    def get_solutions(self, db: Session = Depends(get_db)):
        return solution_service.get_solutions_service(db)

    def get_solution(
        self,
        solution_id: int,
        db: Session = Depends(get_db)
    ):
        result = solution_service.get_solution_service(db, solution_id)

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Solution not found"
            )

        return result

    def update_solution(
        self,
        solution_id: int,
        solution: SolutionCreate,
        db: Session = Depends(get_db)
    ):
        result = solution_service.update_solution_service(
            db, solution_id, solution
        )

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Solution not found"
            )

        return result

    def delete_solution(
        self,
        solution_id: int,
        db: Session = Depends(get_db)
    ):
        result = solution_service.delete_solution_service(
            db, solution_id
        )

        if not result:
            raise HTTPException(
                status_code=404,
                detail="Solution not found"
            )

        return {"message": "Solution deleted successfully"}


solution_api = SolutionAPI()

router.add_api_route(
    "/",
    solution_api.create_solution,
    methods=["POST"],
    response_model=SolutionResponse
)

router.add_api_route(
    "/",
    solution_api.get_solutions,
    methods=["GET"],
    response_model=list[SolutionResponse]
)

router.add_api_route(
    "/{solution_id}",
    solution_api.get_solution,
    methods=["GET"],
    response_model=SolutionResponse
)

router.add_api_route(
    "/{solution_id}",
    solution_api.update_solution,
    methods=["PUT"],
    response_model=SolutionResponse
)

router.add_api_route(
    "/{solution_id}",
    solution_api.delete_solution,
    methods=["DELETE"]
)
