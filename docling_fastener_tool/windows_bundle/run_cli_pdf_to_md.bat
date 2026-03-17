@echo off
REM ===========================================
REM PDF -> MD Docling CLI (Windows)
REM ===========================================
REM Bu dosyayi CIFT TIKLAYARAK calistir.
REM
REM python/pdf_to_md_cli.py script'ini calistirir.
REM  - Once install_deps.bat ile bagimliliklari kurmus olman gerekir.

echo.
echo PDF -> MD (Docling CLI)
echo -----------------------

REM Python'i bul (bir ust dizindeki python_embed veya PATH)
IF EXIST "%~dp0..\python_embed\python.exe" (
    set "PYTHON_EXE=%~dp0..\python_embed\python.exe"
) ELSE (
    where python >nul 2>&1
    IF %ERRORLEVEL% EQU 0 (
        for /f "delims=" %%P in ('where python') do (
            set "PYTHON_EXE=%%P"
            goto :found_python
        )
    ) ELSE (
        echo HATA: python.exe bulunamadi. Lutfen:
        echo  - Ya python_embed klasorune Windows embeddable Python'i ac
        echo  - Ya da sistem PATH'ine python ekle
        pause
        exit /b 1
    )
)

:found_python
echo Python: "%PYTHON_EXE%"
echo.

REM Kullanici girdilerini script icinde interaktif olarak soracagiz
echo python\\pdf_to_md_cli.py calistiriliyor...
echo (PDF klasoru ve OCR modu CLI uzerinden sorulacak)
echo.

"%PYTHON_EXE%" "%~dp0..\python\pdf_to_md_cli.py"

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo Islem sirasinda hata olustu.
    pause
    exit /b 1
)

echo.
echo Islem tamamlandi.
echo Ciktilari belirtilen output_md klasorunde kontrol et.
pause

