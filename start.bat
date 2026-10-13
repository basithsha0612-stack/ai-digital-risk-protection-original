@echo off
title Digital Risk Protection Platform (DRP)
echo ======================================================================
echo Starting Digital Risk Protection Platform (DRP)...
echo ======================================================================

:: Add portable Node to PATH
set "PATH=%~dp0tools\node;%PATH%"

:: Run application
python "%~dp0run_app.py"

pause
