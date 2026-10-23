from sqlalchemy.orm import Session
from app.models.solution import Solution
from app.schemas.solution import SolutionCreate


def create_solution(db: Session, solution: SolutionCreate):
    db_solution = Solution(
        name=solution.name,
        description=solution.description
    )

    db.add(db_solution)
    db.commit()
    db.refresh(db_solution)

    return db_solution


def get_solutions(db: Session):
    return db.query(Solution).all()


def get_solution(db: Session, solution_id: int):
    return db.query(Solution).filter(
        Solution.id == solution_id
    ).first()


def update_solution(db: Session, solution_id: int, solution: SolutionCreate):
    db_solution = get_solution(db, solution_id)

    if db_solution:
        db_solution.name = solution.name
        db_solution.description = solution.description

        db.commit()
        db.refresh(db_solution)

    return db_solution


def delete_solution(db: Session, solution_id: int):
    db_solution = get_solution(db, solution_id)

    if db_solution:
        db.delete(db_solution)
        db.commit()

    return db_solution