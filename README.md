<h2 align="center">
  <img src="https://github.com/Windows81/Roblox-Freedom-Distribution/blob/main/Assets/Logo.png" height="20px"/>
  Server List for
  <a href="https://github.com/Windows81/Roblox-Freedom-Distribution">
    Rōblox Freedom Distribution
  </a>
  <img src="https://github.com/Windows81/Roblox-Freedom-Distribution/blob/main/Assets/Logo.png" height="20px"/>
</h2>

***Note:* for latest data, [navigate here](https://github.com/frostyyyy1/Roblox-Freedom-Distribution-Servers/tree/main).**

<!-- STATUS-START -->
## Status Test
Last check: 2026-02-08 15:10:04 UTC

### Online
- **`frostdev.cloud:2005`**

### Offline / Unreachable
- **`172.88.194.43:2005`**
- **`79.208.64.177:2005`**
<!-- STATUS-END -->

[![Status Check](https://github.com/frostyyyy1/Roblox-Freedom-Distribution-Servers/actions/workflows/main.yml/badge.svg?event=workflow_dispatch)](https://github.com/frostyyyy1/Roblox-Freedom-Distribution-Servers/actions/workflows/main.yml)

## What Is This?

This repository contains a community-maintained list of public Roblox Freedom Distribution servers.
All listed servers are checked automatically for availability and must follow the rules below.

## How to Join

1. Choose a server from the list above.

2. Download the [latest build of Freedom Distribution](https://github.com/Windows81/Roblox-Freedom-Distribution/releases/latest).

3. Run one of the commands below, replacing the values as needed:

- `$host` - hostname; can be an IP address or a domain name.
- `$port` - port number; defaults to 2005.
- `$user` - a "user code" which is governed by the server you're joining.  *Public* servers usually let you pick anything you want.

---

Use this if the server has **one RCC service** or does not specify a separate RCC port.

This is usually intended for single-server setups.

```bash
./RFD.exe player -h $host -p $port -u $user
```

Some servers run **multiple RCC services** behind a single web server.
In this setup, you must choose which RCC service to connect to by specifying its port.

Use the `--rcc_port`, `--port`, `-rp` flag to select the desired RCC service:

```bash
./RFD.exe player -h $host -p PORTHERE -rp $rcc_port -u $user
```

## Adding a Server

To add a server to this list, please [open an issue](https://github.com/frostyyyy1/Roblox-Freedom-Distribution-Servers/issues/new?template=add-a-server.md) with the following information:

- IP address or domain name
- Connection port(s), *if different from the default*
- Server-specific `-u` (user-code) rules
- Any additional notes

Once submitted, the server will be checked and added to the list.

## More Information

For detailed documentation, usage examples, and technical information about Roblox Freedom Distribution, see [the project's README page](https://github.com/Windows81/Roblox-Freedom-Distribution).
