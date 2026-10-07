@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0tools\duo_profiles.py" doctor
  goto :end
)
python "%~dp0tools\duo_profiles.py" doctor
:end
echo.
pause
