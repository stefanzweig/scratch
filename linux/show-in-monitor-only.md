# Show the workspaces in external monitor only

I am using xubuntu in my old MacBook Air with an external monitor. the window manager is i3wm. The first workspace lies in internal display which make me hard to check where my mouse is. So I have to configure all the workspaces are shown in the external monitor. the tool of the multiple monitor control is `xrandr`.

By default, xrandr show the monitors information
```shell
xrandr
```
shows

```text
Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 16384 x 16384
eDP-1 connected primary (normal left inverted right x axis y axis)
   1440x900      60.00 +
   1400x900      60.00
   1440x810      60.00
   1368x768      60.00
   1280x800      60.00
   1280x720      60.00
   1024x768      60.00
VGA-1 disconnected (normal left inverted right x axis y axis)
HDMI-1 disconnected (normal left inverted right x axis y axis)
DP-1 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 598mm x 336mm
   1920x1080     60.00*+  74.97    50.00    59.94
   1920x1080i    60.00    50.00    59.94
   1680x1050     59.95
HDMI-2 disconnected (normal left inverted right x axis y axis)
DP-2 disconnected (normal left inverted right x axis y axis)
```

In the information there are eDP-1 and DP-1 connected, which DP-1 is the external one.

In order to show the contents to the external one, the following command is run.

```shell
xrandr --output DP-1 --auto --output eDP-1 --off
```

in which `--output eDP-1 --off` make the internal display off.
