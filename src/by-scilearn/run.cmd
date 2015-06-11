@echo off
:: Copyright (c) 2012 The Chromium Authors. All rights reserved.
:: Use of this source code is governed by a BSD-style license that can be
:: found in the LICENSE file.
setlocal

:: This is required with cygwin only.
PATH=D:\tools\python2\;%~dp0;%PATH%

:: Synchronize the root directory before deferring control back to gclient.py.
:: call "%~dp0\update_depot_tools.bat" %*

set PYTHONPATH=%~dp0src;%PYTHONPATH%
:: Defer control.
python.exe -m org.dbd.scilearn %*
pause