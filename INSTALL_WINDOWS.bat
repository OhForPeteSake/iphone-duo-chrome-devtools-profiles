@echo off
setlocal
cd /d "%~dp0"
echo ==========================================
echo   iPhone Duo Chrome DevTools Profiles
echo          Installer v1.0.2
echo ==========================================
echo.
if not exist "%~dp0tools\duo_profiles.py" (
  echo ERROR: tools\duo_profiles.py is missing.
  pause
  exit /b 2
)
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0tools\duo_profiles.py" install
  goto :end
)
where python >nul 2>nul
if %errorlevel%==0 (
  python "%~dp0tools\duo_profiles.py" install
  goto :end
)
echo ERROR: Python 3 was not found.
:end
echo.
pause
