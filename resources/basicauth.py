import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

class Httpsbasicauth:

    @staticmethod
    def verify_auth(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
        correct_username = credentials.username == os.environ['username']
        correct_password = credentials.password == os.environ['password']
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},)
            return credentials.username

