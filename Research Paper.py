from fastapi import *
from pydantic import *
from typing import *
from starlette import status

app = FastAPI()


class Paper:
    title: str
    author: str
    publish_date: int
    citations: int

    def __init__(self, title, author, publish_date, citations):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.citations = citations


class PaperRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    publish_date: int = Field(gt=0, lt=2027)
    citations: int = Field(gt=-1)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A research title",
                "author": "J.Doe",
                "publish_date": "2012",
                "citations": "11"
            }
        }
    }


PAPERS = [
    Paper("Effects of static electricty on semi_conductors.", "J.Kerins", 2007, 34),
    Paper("Investigating the rate of change of Irish tides.", "B.Simmons", 2023, 12)
]


@app.get("/papers", status_code=status.HTTP_200_OK)
async def show_all_papers():
    return PAPERS


@app.get("/papers/{author}/", status_code=status.HTTP_200_OK)
async def search_by_author(paper_author: str = Path(min_length=1)):
    for paper in PAPERS:
        if paper.author == paper_author:
            return paper
    raise HTTPException(status_code=404, detail="Item Not Found")


@app.get("/papers/publish", status_code=status.HTTP_200_OK)
async def search_by_publish_date(publish_date: int = Query(gt=0, lt=2027)):
    papers_to_return = []
    for paper in PAPERS:
        if paper.publish_date == publish_date:
            papers_to_return.append(paper)
        return papers_to_return


@app.post("/create_paper", status_code=status.HTTP_201_CREATED)
async def create_paper(paper_request: PaperRequest):
    new_paper = Paper(**paper_request.model_dump())
    PAPERS.append(new_paper)


@app.put("/papers/update_paper", status_code=status.HTTP_204_NO_CONTENT)
async def update_paper(paper: PaperRequest):
    paper_changed = False
    for i in range(len(PAPERS)):
        if PAPERS[i].title == paper.title:
            PAPERS[i] = paper
            paper_changed = True
            return paper
    if not paper_changed:
        raise HTTPException(status_code=404, detail="Item Not Found")
