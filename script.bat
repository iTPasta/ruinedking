cd JeuPygameCMI
@ECHO off
@SET MY_VAR=
FOR /F %%I IN ('cd') DO @SET "MY_VAR=%%I"
ECHO %MY_VAR%
py main.py %MY_VAR%