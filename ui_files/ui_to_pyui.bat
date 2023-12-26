pyuic5 main_window.ui -o ..\python_ui_files\main_window_ui.py
REM pyuic5 triggers_window.ui -o ..\python_ui_files\triggers_window_ui.py
REM pyuic5 connections_window.ui -o ..\python_ui_files\connections_window_ui.py
REM pyrcc5 ..\res\res.qrc -o ..\res\resources_rc.py

REM Replace the string "import res_rc" with "import GUI.res.resources_rc"
powershell -Command "(Get-Content ..\python_ui_files\main_window_ui.py) -replace 'import res_rc', 'import GUI.res.resources_rc' | Set-Content ..\python_ui_files\main_window_ui.py"
REM powershell -Command "(Get-Content ..\python_ui_files\triggers_window_ui.py) -replace 'import res_rc', 'import GUI.res.resources_rc' | Set-Content ..\python_ui_files\triggers_window_ui.py"
REM powershell -Command "(Get-Content ..\python_ui_files\connections_window_ui.py) -replace 'import res_rc', 'import GUI.res.resources_rc' | Set-Content ..\python_ui_files\connections_window_ui.py"
