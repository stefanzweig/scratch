# How to center the active window with AHK

The script is as below.

```shell
#NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn ; Enable warnings to assist with detecting common errors.
SendMode Input ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.

PositionToggle = 1 ; Use a number as a toggle for marking on which monitor the window should appear.

^y::
 WinGetTitle, ActiveWindowTitle, A
 WinGetPos,,, Width, Height, %ActiveWindowTitle%
 
 If PositionToggle = 1 ; Check the toggle's state and "do what's between the curly brackets" if it's set to 1 for our primary monitor.
 {
 TargetX := (A_ScreenWidth/2)-(Width/2)
 TargetY := (A_ScreenHeight/2)-(Height/2)

 PositionToggle = 2 ; "Flick" the toggle so that if we reuse the hotkey, our active window will move to the second monitor.
 }
 Else If PositionToggle = 2 ; Have we used the hotkey before, "flicking" the toggle number to the second monitor? Then the script should instead do what's between the following curly brackets instead of the ones above.
 {
 SysGet, Mon2, Monitor, 2 ; Get the second monitor's details
 Mon2Width := Mon2Right - Mon2Left ; Calculate the second monitor's actual width.
 Mon2Height := Mon2Bottom - Mon2Top ; Calculate the second monitor's actual height.
 
 TargetX := (Mon2Width/2)-(Width/2)+A_ScreenWidth ; Calculate where to move the window. Notice that we also add the primary monitor's width since AutoHotKey can't move windows on individual monitors but across their combined "surface".
 TargetY := (Mon2Height/2)-(Height/2)+Mon2Top ; Calculate the optimal vertical target for moving the window on the second monitor. Like above, the second monitor's vertical details are detected in relation to the primary monitor. Thus, we have to get creative to get an optimal target by acknowledging how the second monitor's top isn't equal to 0 (like the primary one's).
 
 PositionToggle = 1 ; Flick the toggle back so that if we reuse the hotkey, the window will move back to the primary monitor.
 }
 
 WinMove, %ActiveWindowTitle%,, %TargetX%, %TargetY% ; The actual action, moving the active window to our calculated coordinates.
 
return
```