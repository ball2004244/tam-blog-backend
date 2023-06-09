from fastapi import HTTPException
def handle_error(obj: object = None, e: Exception = None) -> None:
    if not obj:
        raise HTTPException(status_code=404, detail='Internal Error: %s' % str(e))
    
    if str(obj['status_code'])[0] != '2':
        raise HTTPException(status_code=obj['status_code'], detail=obj['error'])