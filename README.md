# Mikrotik HTML Dumper

---

This is a small project written since my team worked with mikrotiks and we sometimes needed to present audits of the configuration for upper manangement in a quick and easy to read format.

## Installing

You can use pip to install this script

```pip install mikrtotikhtml```

## Requirements

You'll need to setup a .env file for the username and password. You can do so by running the following command

```mikrotikthml create-env-file -c```

It will then ask you to enter the username and password which will be stored in a .env file for you from the current working directory of the script.


# Usage

---

To use the script, simply run the following

```mikrotikhtml html-dump```

It will then ask you to enter the IP or FQDN of the firewall and dump out HTML code so you can easily upload to markup language supported documentation systems, or simply share it as a web file.

# License

---

MIT




