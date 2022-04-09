from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from aiohttp import ClientResponse

class UniverselistException(Exception):
    
class ClientException(UniverselistException):
    
class TokenNotDetected(UniverselistException):
    

class HTTPException(UniverselistException):
    def __init__(
        self,
        response: "ClientResponse",
        data: Union[dict, str]
    ) -> None:
    self.response = response
    
    if isinstance(data, dict):
        self.status = data.get("status", 0)
        self.message = data.get("message", "")
    else:
        self.message = data
        
    formatting = f"{self.response.status}: {self.response.reason}"
    if self.message:
        formatting = f"{self.status}: {self.message}"
        
    super().__init__(formatting)
    
class Unauthorized(HTTPException):
    
class NotFound(HTTPException):
    
class ServerException(HTTPException):