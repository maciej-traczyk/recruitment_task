@echo off
setlocal enabledelayedexpansion

cd /d "%SRC_DIR%"

"%PYTHON%" -m pip install . ^
    --no-deps ^
    --no-build-isolation ^
    -vv

if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%