from fastapi.responses import FileResponse
from leeFU.LeeFileManager import LeeFileManager


class PhotoManager:
    async def upload(self, file, title):
        filename = await LeeFileManager.upload("./photo/files/", file, "uuid")
        return {"title": title, "file": filename}
    def get(self,filename):
        return FileResponse('./photo/files/'+filename,filename=filename)