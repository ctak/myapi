from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database import SessionLocal
from database import get_db
# from models import Question

from domain.question import question_schema, question_crud

# p
router = APIRouter(
  prefix="/api/question",
)

@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
  ## SessionLocal을 사용하여 DB에 접근하는 방법
  # db = SessionLocal()
  # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
  # db.close() # 이걸 꼭 해야하나 보지? => Pool에 돌려주는 것이니 괜찮다.
  #
  # # 제너레이터 사용
  # with get_db() as db:
  #     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
  #
  # # Depends 사용
  # but @contextlib.contextmanager 를 주석 처리해야 함.
  # > FastAPI는 제너레이터 기반 함수를 직접 지원하며, 자동으로 리소스 관리를 처리한다. 
  # > 그러나 @contextlib.contextmanager를 사용하면 get_db 함수가 contextlib._GeneratorContextManager 객체를 반환하게 되어 
  # > FastAPI의 종속성 주입이 제대로 동작하지 않는다. 따라서 get_db 함수에서 @contextlib.contextmanager 어노테이션을 제거해야 한다
  # 
  
  _question_list = question_crud.get_question_list(db)
  return _question_list

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question