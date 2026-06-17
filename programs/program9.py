from pydantic import BaseModel
import wikipediaapi

# Define Pydantic Schema
class Institution(BaseModel):
    name: str
    summary: str

# Initialize Wikipedia API
wiki = wikipediaapi.Wikipedia(
    user_agent="MyBot/1.0",
    language="en"
)

name = input("Enter institution name: ")
page = wiki.page(name)

if page.exists():
    # Parse data into Pydantic model
    data = Institution(
        name=name,
        summary=page.summary[:200]
    )
    print(data.model_dump_json(indent=2))
else:
    print("Page not found")
