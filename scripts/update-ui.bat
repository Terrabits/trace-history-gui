@echo off
setlocal
SET "ROOT_DIR=%~dp0.."
cd /d "%ROOT_DIR%"


REM paths
SET "INPUT_DIR=%ROOT_DIR%\qtcreator"
SET "OUTPUT_DIR=%ROOT_DIR%\trace_history_gui\widgets"


REM update

cd /d qtcreator

for %%f in (*.ui) do (
  del /Q "%OUTPUT_DIR%\ui_*.py"
  pyside2-uic --output "%OUTPUT_DIR%\ui_%%~nf.py" "%INPUT_DIR%\%%~nf.ui"
)
