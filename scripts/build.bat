@echo off
setlocal
SET "ROOT_DIR=%~dp0.."
cd /d "%ROOT_DIR%"


REM build
REM call scripts\update-ui.bat
pyinstaller pyinstaller-win.spec %*
