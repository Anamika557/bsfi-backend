from sqlalchemy.orm import Session
from app import crud
from app.schemas.solution import SolutionCreate


def create_solution_service(db: Session, solution: SolutionCreate):
    return crud.solution.create_solution(db, solution)


def get_solutions_service(db: Session):
    return crud.solution.get_solutions(db)


def get_solution_service(db: Session, solution_id: int):
    return crud.solution.get_solution(db, solution_id)


def update_solution_service(
    db: Session,
    solution_id: int,
    solution: SolutionCreate
):
    return crud.solution.update_solution(db, solution_id, solution)


def delete_solution_service(db: Session, solution_id: int):
    return crud.solution.delete_solution(db, solution_id)