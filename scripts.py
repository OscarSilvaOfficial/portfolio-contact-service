import os
import typer
from typing import Optional

app = typer.Typer(help="Awesome CLI user manager.")

@app.command()
def server(port: Optional[str] = 8000):
  os.system('uvicorn main:app --reload --port {}'.format(port))
  
@app.command()
def tests():
  os.system('pytest')
  
if __name__ == "__main__":
    app()