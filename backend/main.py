
import uvicorn
from app.server import app
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8100, reload=True, workers=1)