#### Simple python D-Bus API to control systemd services

This was forked from [systemd-manager](https://github.com/emlid/systemd-manager). This fork adds a couple of methods and changes the way errors are handled.

##### Prerequisities

This packages uses D-Bus to control systemd. You need to have D-Bus itself and its python bindings in order to use this library. For example, on Ubuntu you need to install the following packages:

`sudo apt install dbus libdbus-glib-1-dev libdbus-1-dev python-dbus`

The setup.py **does not contain** the `python-dbus` dependency and you have to install it manually.

##### Example

```
from systemd_manager import SystemdManager

manager = SystemdManager()
if not manager.is_active("bluetooth.service"):
    manager.start_unit("bluetooth.service")

```

##### API

* `SystemdManager().list_units()`
* `SystemdManager().list_jobs()`
* `SystemdManager().start_unit(unit_name, mode="replace")`
	* `unit_name` - a string in form of `'*.service'`
	* `mode` - start mode. One of `replace`, `fail`, `isolate`, `ignore-dependencies`, `ignore-requirements`. Details [here](https://www.freedesktop.org/wiki/Software/systemd/dbus/)
	* returns bool representing operation success
* `SystemdManager().stop_unit(unit_name, mode="replace")`
	* `unit_name` - a string in form of `'*.service'`
	* `mode` - start mode. One of `replace`, `fail`, `isolate`, `ignore-dependencies`, `ignore-requirements`. Details [here](https://www.freedesktop.org/wiki/Software/systemd/dbus/)
	* returns bool representing operation success
* `SystemdManager().enable_unit(unit_name)`
	* `unit_name` - a string in form of `'*.service'`
	* returns bool representing operation success
* `SystemdManager().disable_unit(unit_name)`
	* `unit_name` - a string in form of `'*.service'`
	* returns bool representing operation success
* `SystemdManager().is_active(unit_name)`
	* `unit_name` - a string in form of `'*.service'`
	* returns bool representing unit state

##### Credits

This package was originally written by [Aleksandr Aleksandrov](https://github.com/AD-Aleksandrov).
